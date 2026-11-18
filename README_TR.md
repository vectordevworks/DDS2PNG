# DDS'den PNG'ye Dönüştürücü

<a href="README.md">
  <img src="https://flagcdn.com/gb.svg" width="20" alt="İngilizce"> İngilizce
</a>
|
<a href="README_DE.md">
  <img src="https://flagcdn.com/de.svg" width="20" alt="Almanca"> Almanca
</a>
|
<a href="README_ES.md">
  <img src="https://flagcdn.com/es.svg" width="20" alt="İspanyolca"> İspanyolca
</a>
|
<a href="README_FR.md">
  <img src="https://flagcdn.com/fr.svg" width="20" alt="Fransızca"> Fransızca
</a>
|
<a href="README_JA.md">
  <img src="https://flagcdn.com/jp.svg" width="20" alt="Japonca"> Japonca
</a>
|
<a href="README_KO.md">
  <img src="https://flagcdn.com/kr.svg" width="20" alt="Korece"> Korece
</a>
|
<a href="README_PT.md">
  <img src="https://flagcdn.com/pt.svg" width="20" alt="Portekizce"> Portekizce
</a>
|
<a href="README_RU.md">
  <img src="https://flagcdn.com/ru.svg" width="20" alt="Rusça"> Rusça
</a>
|
<a href="README_ZH_CN.md">
  <img src="https://flagcdn.com/cn.svg" width="20" alt="Basitleştirilmiş Çince"> Basitleştirilmiş Çince
</a>
|
<a href="README_TR.md">
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe
</a>

Basit bir grafik arayüzüne sahip, Python tabanlı hafif bir DDS'den PNG'ye dönüştürme aracı.

## Genel Bakış

DDS to PNG Converter, DDS (DirectDraw Surface) biçimindeki doku dosyalarını sezgisel bir grafik arayüzü aracılığıyla PNG görüntülerine dönüştürmek için geliştirilmiş bir masaüstü uygulamasıdır.

Projenin amacı, kullanıcıların komut satırı komutlarıyla uğraşmasına gerek kalmadan doku dosyalarını kolay ve pratik bir şekilde dönüştürebilmesini sağlamaktır.

## Özellikler

- DDS dosyalarını PNG biçimine dönüştürme.
- Basit ve kullanıcı dostu grafik arayüzü.
- Python tabanlı, hafif uygulama.
- Kolay dosya seçimi ve dönüştürme süreci.

## Gereksinimler

- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv): DDS dosyalarını PNG formatına dönüştürmek için kullanılır. Uygulamayla birlikte `assets` klasöründe sunulur.

### Texconv (İsteğe Bağlı İndirme)

Projeyle birlikte sunulan Texconv çalışmazsa veya manuel olarak indirmek isterseniz aşağıdaki yöntemleri kullanabilirsiniz.

**PowerShell (Winget):**

```powershell
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Kurulumu kontrol etmek için:

```powershell
winget list --id Microsoft.DirectXTex.Texconv
```

**Manuel İndirme:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/vectordevworks/DDS2PNG.git
   ```

2. Proje dizinine gidin:

   ```bash
   cd "PROJE DOSYA YOLU"
   ```

3. Gerekli bağımlılıkları yükleyin:

   ```powershell
   pip install -r requirements.txt
   ```

### Sanal Ortam (İsteğe Bağlı)

Python bağımlılıklarını diğer projelerden ayrı tutmak için sanal ortam kullanabilirsiniz.

1. (Yalnızca PowerShell betik çalıştırma hatası verirse) geçerli oturum için geçici izin verin:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

2. Sanal ortam oluşturun:

   ```powershell
   python -m venv .venv
   ```

3. Sanal ortamı etkinleştirin:

   ```powershell
   .venv\Scripts\activate
   ```

4. Gerekli bağımlılıkları yükleyin:

   ```powershell
   python -m pip install -r requirements.txt
   ```

5. İşiniz bittiğinde sanal ortamdan çıkın:
 
   ```powershell
    deactivate 
## Kurulum

1. Depoyu klonlayın:

   ```bash
   git clone https://github.com/vectordevworks/DDS-to-PNG-Converter.git
   ```

2. Proje dizinine gidin:

   ```bash
   cd "PROJE DOSYA YOLU"
   ```

## Kullanım

Uygulamayı çalıştırın:

```bash
python Converter.pyw
```

DDS dosyanızı seçin ve PNG biçimine dönüştürmek için ekrandaki talimatları izleyin.

## Derleme (EXE Oluşturma)

Python uygulamasını tek bir EXE dosyasına dönüştürmek için aşağıdaki adımları izleyin.

**Önemli:** PowerShell'i yönetici olarak değil, normal kullanıcı olarak çalıştırın. Yönetici izinlerine ihtiyaç yoktur.

### 1. PowerShell'i Açma

1. Windows Başlat menüsünü açın.
2. Arama bölümüne `PowerShell` veya `Windows Terminal` yazın.
3. Windows PowerShell'i veya Windows Terminal'i normal şekilde açın.
4. Yönetici olarak çalıştır seçeneğini kullanmayın.

### 2. Proje Klasörüne Geçiş

PowerShell'e aşağıdaki komutu girerek proje klasörüne geçin:

```powershell
cd "D:\vectorrdevworks\Projeler\Yazılım Projeleri\Python\DDS-to-PNG-Converter"
```

### 3. Uygulama İkonunu Gömme

Aşağıdaki komut, `embed_icon.ps1` betiğini çalıştırarak uygulama ikonunu Python dosyasına gömer.

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Not:** Windows'un PowerShell betiklerini çalıştırmasını engelleyen yürütme ilkesi nedeniyle `-ExecutionPolicy Bypass` kullanılır. Bu ayar yalnızca başlatılan PowerShell işlemi için geçerlidir. Sistem genelindeki güvenlik ayarları değiştirilmez.

### 4. PyInstaller ile Derleme

İkon gömme işlemi tamamlandıktan sonra aşağıdaki komutu çalıştırarak EXE dosyasını oluşturun:

```powershell
py -m PyInstaller --noconfirm --clean --onefile --windowed --icon="assets\icon.ico" --name "DDS-to-PNG-Converter" "Converter.pyw"
```

**Komut parametreleri:**

| Parametre | Açıklama |
|---|---|
| `--noconfirm` | Onay istemeden derleme yapar. |
| `--clean` | Önceki derleme önbelleğini temizler. |
| `--onefile` | Tek bir EXE dosyası oluşturur. |
| `--windowed` | Konsol penceresini göstermez. |
| `--icon` | EXE dosyasının ikonunu belirler. |
| `--name` | Oluşturulacak EXE dosyasının adını belirler. |

### 5. Derleme Çıktısı

Derleme başarıyla tamamlandığında EXE dosyası aşağıdaki klasörde oluşturulur:

```text
dist\DDS-to-PNG-Converter.exe
```

**Yeni bir sürüm derlerken sıralama:**

1. PowerShell'i normal kullanıcı olarak açın.
2. Proje klasörüne geçin.
3. İkon gömme komutunu çalıştırın.
4. PyInstaller derleme komutunu çalıştırın.
5. Oluşturulan EXE dosyasını `dist` klasöründen alın.

## Geliştirici

**vectordevworks**

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.