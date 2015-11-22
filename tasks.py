import luigi
from path import Path
import sh
import shlex

download_pth = Path('download').abspath()

class FilePath(luigi.Parameter):
    def parse(self, value):
        return Path(value)

class Reads(luigi.Task):
    r1 = luigi.Parameter()
    r2 = luigi.Parameter(default=False)

    def output(self):
        o = []
        o.append(luigi.LocalTarget(self.r1))
        if self.r2:
            o.append(luigi.LocalTarget(self.r2))
        return o

class BowtieBuild(luigi.Task):
    input_fasta = luigi.Parameter()
    bowtie_build_path = luigi.Parameter(default=sh.which('bowtie2-build'))
    bowtie_build_options = luigi.Parameter(default='')
    
    def run(self):
        bowtie_build_exe = sh.Command(self.bowtie_build_path)
        args = '{0} {1} {2}'.format(
            self.bowtie_build_options, self.input_fasta, 'bowtie_index'
        )
        print bowtie_build_exe(shlex.split(args))

    def output(self):
        return luigi.LocalTarget('bowtie_index.1.bt2')

class BowtieAlign(luigi.Task):
    forward_reads = luigi.Parameter()
    reverse_reads = luigi.Parameter(default=False)
    bowtie_path = luigi.Parameter(default=sh.which('bowtie2'))
    bowtie_options = luigi.Parameter(default='')

    def requires(self):
        return BowtieBuild()

    def run(self):
        bowtie = sh.Command(self.bowtie_path)
        args = '{0} -x {1}'.format(
            self.bowtie_options, self.forward_reads
        )
        if self.reverse_reads:
            args += ' -1 {1} -2 {2}'.format(self.forward_reads, self.reverse_reads)
        else:
            args += ' -U {0}'.format(self.forward_reads)
        args += ' -S bowtie-output.sam'
        print bowtie(shlex.split(args))

    def output(self):
        return luigi.LocalTarget('bowtie-output.sam')
