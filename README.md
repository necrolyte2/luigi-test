# Luigi Testing

Just a simple bowtie luigi task chain

# Setup

```
pip install -r requirements.txt
export PATH=$PATH:download/bowtie2-2.2.6
export PYTHONPATH=$PWD
```

# Run Task

## Run single fasta file

```
luigi --module tasks BowtieAlign \
    --BowtieAlign-forward-reads r1.fasta \
    --BowtieBuild-input-fasta r1.fasta \
    --local-scheduler
```

## Run single fasta file

```
luigi --module tasks BowtieAlign \
    --BowtieAlign-forward-reads r1.fasta \
    --BowtieAlign-reverse-reads r2.fasta \
    --BowtieBuild-input-fasta r1.fasta \
    --BowtieAlign-bowtie-options '\-f' \
    --local-scheduler
```
