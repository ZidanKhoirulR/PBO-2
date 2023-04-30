def calculate_average(numbers):
    try:
        assert len(numbers) > 0, "List harus memiliki setidaknya satu elemen"
        return sum(numbers) / len(numbers)
    except AssertionError as error:
        print(f"Terjadi kesalahan: {error}")


# Panggil fungsi calculate_average dengan argumen yang tidak valid
result = calculate_average([])
