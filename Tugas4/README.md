# Tugas 4

## Dokumentasi Protokol

### Ketentuan membaca format

string terbagi menjadi 2 bagian yang dipisahkan oleh spasi
Format : command *spasi* parameter *spasi* parameter

### Fitur-fitur :

1. Meletakkan file
    * Request: put
    * Parameter: namafile *spasi* isifile
    * Response:
        * Jika Berhasil  -> "File Berhasil Ditaruh"
        * Jika Gagal     -> "ERROR"

2. Mengambil file
    * Request: get
    * Parameter: namafile
    * Response: isi file dalam bentuk base64encode "format dan file sudah diterima"

3. Melihat list file
    * Request: list
    * Parameter: tidak ada
    * Response: daftar nama file yang ada pada folder result dalam bentuk **json** format

4. Jika _command_ tidak dikenali akan merespon dengan ERRCMD

## Laporan

  ### 1. Meletakan file
  * a -> screenshoot folder keseluruhan, File yang akan ditaruh ke folder result adalah bob.jpg dan cobain.txt
  * b -> screenshoot kondisi folder result sebelum program dijalankan
  * c -> menjalankan server.py dan putfile.py
  * d -> screenshoot kondisi folder result setelah program dijalanankan

  ### 2. Mengambil file
  * a -> screenshoot folder result, file bob.jpg dan cobain.txt yang akan di getfile
  * b -> screenshoot folder keseluruhan, file bob.jpg dan cobain.txt yang akan di getfile sudah di delete di folder keseluruhan
  * c -> menjalankan server.py dan getfile.py
  * d -> screenshoot kondisi folder setelah program dijalankan

  ### 3. List File
  * a -> screenshoot folder result saat ini, sekarang berisi bob.jpg dan cobain.txt
  * b -> screenshoot saat menjalankan server.py dan listfile.py
