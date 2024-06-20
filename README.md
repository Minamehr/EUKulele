# EUKulele

## Test locally with

```
cd /EUKulele/test-data
EUKulele -s MAGs_input -o output -m mags --ref_fasta /home/paul/git/people/mina/EUKulele/test-data/test_db/reference-pep-trunc.pep.faa --tax_table test_db/tax-table.txt --protein_map test_db/protein-map.json --alignment_choice diamond --n_ext .faa  --consensus_cutoff 0.75
```