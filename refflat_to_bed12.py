#!/usr/bin/env python
#===============================================================================
# refflat_to_bed12.py
#===============================================================================

from argparse import ArgumentParser
import pandas as pd

def parse_arguments():
    parser = ArgumentParser(description='convert refflat to bed12')
    parser.add_argument('refflat')
    return parser.parse_args()

def main():
    args = parse_arguments()
    refflat = pd.read_table(args.refflat, header=None)
    for _, (gene, _, chrom, strand, start, end, thick_start, thick_end, exon_count, exon_starts, exon_ends) in refflat.iterrows():
        exon_sizes = ','.join(str(e - s) for s, e in zip((int(x) for x in exon_starts[:-1].split(',')), (int(x) for x in exon_ends[:-1].split(','))))+','
        exon_starts_relative = ','.join(str(int(s) - int(start)) for s in exon_starts[:-1].split(',')) + ','
        print(chrom, start, end, gene, '.', strand, thick_start, thick_end, '0,0,0', exon_count, exon_sizes, exon_starts_relative, sep='\t')



if __name__ == '__main__':
    main()
