"""Rough memory needed just to hold a model's weights.
Excludes the working memory used while generating text and runtime overhead, so real use needs more."""

BYTES_PER_PARAMETER = {"16-bit": 2.0, "8-bit": 1.0, "4-bit": 0.5}


def weight_gigabytes(billions_of_parameters, precision):
    return billions_of_parameters * BYTES_PER_PARAMETER[precision]   # 1e9 params * bytes = GB


if __name__ == "__main__":
    for size in (7, 13, 70):
        row = ", ".join(f"{p}: {weight_gigabytes(size, p):.1f} GB" for p in BYTES_PER_PARAMETER)
        print(f"{size}B parameters -> {row}")
