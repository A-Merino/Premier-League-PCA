import graphing as grph
import analysis as an
import parsing as prs
import utils as ut


def main():

    # Get paths to all data files then
    # Get all data in one pandas DF
    data = prs.get_all_data(ut.get_file_paths())

    # data, year = prs.get_year_data(2024)
    # print(data)
    an.compute_pca(data, 0)
    # pca_data = an.compute_pca(data)

    # pca_gk = an.compute_pos_pca(data, "GK")
    # pca_df = an.compute_pos_pca(data, "DF")


main()
