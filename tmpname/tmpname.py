#!/usr/bin/env python3

import os
import tmpname

def annotate_ins(vcf, 
                 wk_dir, 
                 species, 
                 threads, 
                 mafft_exe=None, 
                 ins_seq='ins_seq.fa', 
                 sv_sup='sv_support_reads.tsv'
                 ):
    tmpname.check_args(species)
    mafft_exe = tmpname.check_exe(mafft_exe, 'mafft') 
    id_seq, fasta_dir = tmpname.create_fa(vcf, wk_dir, sv_sup, ins_seq)
    samplename, threads_per_job= tmpname.create_cons(vcf, wk_dir, fasta_dir, id_seq, threads, mafft_exe, batch_size=100, num_parallel_workers=5)
    tmpname.rep_annote(wk_dir, samplename, threads_per_job, species)

def main():
    args = tmpname.get_args()
    # Check working directory
    if not os.path.exists(args.dir):
          os.makedirs(args.dir)
    annotate_ins(args.vcf, args.dir, args.species, args.threads, args.mafftpath, args.insfa, args.suptsv)

if __name__ == "__main__":
    main()
