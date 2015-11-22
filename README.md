# Luigi Testing

Just a simple bowtie luigi task chain

# Setup

```
pip install -r requirements.txt
```

# Run Task

```
PATH=$PATH:download/bowtie2-2.2.6
PYTHONPATH=$PWD
luigi --module tasks BowtieAlign --BowtieAlign-forward-reads test.fasta --BowtieBuild-input-fasta test.fasta --local-scheduler
```
