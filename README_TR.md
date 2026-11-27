
<div align="center">

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
<strong>
  <img src="https://flagcdn.com/tr.svg" width="20" alt="Türkçe"> Türkçe
</strong>

</div>

# DDS'den PNG'ye Dönüştürücü

DDS'den PNG'ye Dönüştürücü, DDS (DirectDraw Surface) biçimindeki doku dosyalarını PNG görüntülerine dönüştürmenizi sağlayan, Python tabanlı hafif bir masaüstü uygulamasıdır. Basit grafik arayüzü sayesinde dosyalarınızı kolayca seçebilir ve dönüştürme işlemini gerçekleştirebilirsiniz.

---

## İçindekiler

<div align="center">

<div align="center">

<a href="#-genel-bakis">🔍 Genel Bakış</a> |
<a href="#-ozellikler">✨ Özellikler</a> |
<a href="#-gereksinimler">📋 Gereksinimler</a> |
<a href="#-kurulum">📥 Kurulum</a> |
<a href="#-sanal-ortam-istege-bagli">🐍 Sanal Ortam</a> |
<a href="#-kullanim">🚀 Kullanım</a> |
<a href="#-derleme-exe-olusturma">📦 Derleme (EXE)</a> |
<a href="#-gelistirici">👨‍💻 Geliştirici</a> |
<a href="#-lisans">📄 Lisans</a>

</div>

</div>

---

## Genel Bakış

Uygulama, DDS biçimindeki doku dosyalarını Microsoft DirectXTex (Texconv) aracılığıyla PNG formatına dönüştürür. Dönüştürme işlemi grafik arayüzü üzerinden gerçekleştirilir; komut satırı komutlarıyla uğraşmanız gerekmez.

Texconv aracı uygulamayla birlikte `assets` klasöründe sunulur.

## Özellikler

- **DDS'den PNG'ye dönüştürme:** DDS dosyalarını PNG formatına dönüştürür.
- **Grafik arayüz:** Dosya seçme ve dönüştürme işlemlerini kolaylaştıran basit bir arayüz sunar.
- **Texconv desteği:** DDS dosyalarının dönüştürülmesi için Microsoft DirectXTex aracını kullanır.
- **Kolay kullanım:** Dönüştürme işlemini komut satırı kullanmadan gerçekleştirmenizi sağlar.

## Gereksinimler

- Windows
- Python 3.x
- Pillow
- Microsoft DirectXTex (Texconv)

`tkinter`, `ctypes`, `json`, `math`, `os` ve `pathlib` modülleri Python standart kütüphanesinin bir parçasıdır.

Texconv, DDS dosyalarını PNG formatına dönüştürmek için kullanılır ve uygulamayla birlikte `assets` klasöründe sunulur.

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

2. Proje klasörünü açın.
3. PowerShell'i proje klasöründe başlatın.
4. Gerekli Python paketlerini yükleyin:

```powershell
py -m pip install -r requirements.txt
```

## Sanal Ortam (İsteğe Bağlı)

Python bağımlılıklarını diğer projelerden ayrı tutmak için sanal ortam kullanabilirsiniz.

1. Sanal ortam oluşturun:

```powershell
py -m venv .venv
```

2. Sanal ortamı etkinleştirin:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Gerekli bağımlılıkları yükleyin:

```powershell
py -m pip install -r requirements.txt
```

4. İşiniz bittiğinde sanal ortamı devre dışı bırakın:

```powershell
deactivate
```

**CMD (Komut İstemi) üzerinden etkinleştirme:**

PowerShell yerine CMD kullanıyorsanız:

```cmd
.venv\Scripts\activate.bat
```

Sanal ortamdan çıkmak için:

```cmd
deactivate
```

### Sanal Ortam Etkinleştirme Sorunları

Bazı durumlarda PowerShell, güvenlik ilkesi (Execution Policy) nedeniyle sanal ortamı etkinleştirmeyi engelleyebilir.

Bu durumda aşağıdaki komutu çalıştırabilirsiniz:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Ardından sanal ortamı tekrar etkinleştirin:

```powershell
.\.venv\Scripts\Activate.ps1
```

Bu ayar yalnızca açık olan PowerShell oturumu için geçerlidir. Yeni bir PowerShell oturumu açıldığında varsayılan ayarlar yeniden uygulanır.

### Sanal Ortamı Etkinleştirmeden Kullanma

Sanal ortamı etkinleştirmek zorunlu değildir. Etkinleştirme işlemi başarısız olursa Python ve pip dosyalarını doğrudan çağırarak sanal ortamı kullanmaya devam edebilirsiniz.

**Bağımlılıkları yüklemek için:**

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Uygulamayı çalıştırmak için:**

```powershell
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Not:** Sanal ortam oluşturma, etkinleştirme, bağımlılıkları yükleme ve devre dışı bırakma işlemleri için yönetici izni gerekmez. Ancak Python'un doğru şekilde kurulu olması ve gerekli dosyalara erişim izninizin bulunması gerekir.

## Kullanım

1. `DDSConverter.pyw` dosyasını çalıştırın:

```powershell
pyw .\DDSConverter.pyw
```

Alternatif olarak:

```powershell
pythonw .\DDSConverter.pyw
```

2. Dönüştürmek istediğiniz DDS dosyasını seçin.
3. Çıktı klasörü olarak mevcut `convert` klasörünü seçebilir veya dilediğiniz klasörü belirleyebilirsiniz.
4. PNG formatına dönüştürme işlemini gerçekleştirin.

## Derleme (EXE Oluşturma)

Python uygulamasını tek bir EXE dosyasına dönüştürmek için PyInstaller kullanılır.

### 1. Proje Klasörüne Geçiş

Öncelikle DDS2PNG proje klasörünü açın. Terminali proje klasöründe başlatmak için aşağıdaki yöntemlerden birini kullanabilirsiniz.

**Yöntem 1: Dosya Gezgini üzerinden terminal açma**

1. DDS2PNG proje klasörünü Dosya Gezgini üzerinden açın.
2. Adres çubuğuna `cmd` veya `powershell` yazın.
3. Enter tuşuna basın.

Böylece terminal doğrudan proje klasöründe açılır.

**Yöntem 2: Terminal üzerinden proje klasörüne geçme**

CMD veya PowerShell'i açın ve aşağıdaki komutlardan uygun olanı kullanın.

**CMD (Komut İstemi):**

```cmd
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```powershell
Set-Location -LiteralPath "PROJE_KLASORUNUN_YOLU"
```

`PROJE_KLASORUNUN_YOLU` bölümünü kendi bilgisayarınızdaki DDS2PNG proje klasörünün tam konumuyla değiştirin.

**Not:** Yönetici olarak çalıştırmanız gerekmez. Normal kullanıcı yetkileri yeterlidir.

### 2. EXE Derleme

Proje içerisinde bulunan `scripts` klasöründeki `buid.ps1` betiği, PyInstaller kullanarak uygulamayı EXE formatında derler.

Derleme betiği aşağıdaki işlemleri otomatik olarak gerçekleştirir:

- Gerekli proje dosyalarını kontrol eder.
- PyInstaller kurulumunu kontrol eder.
- Önceki derleme dosyalarını temizler.
- `icon.ico` dosyasını EXE simgesi olarak kullanır.
- `assets` klasörünü EXE dosyasına dahil eder.
- Derleme çıktısını kontrol eder.

**CMD üzerinden çalıştırma:**

```cmd
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**PowerShell üzerinden çalıştırma:**

```powershell
.\scripts\buid.ps1
```

### 3. Derleme Çıktısı

Derleme başarıyla tamamlandığında EXE dosyası aşağıdaki konumda oluşturulur:

```text
dist\DDS2PNG.exe
```

**Yeni bir sürüm derlemek için izlenecek adımlar:**

1. DDS2PNG proje klasörünü açın.
2. Adres çubuğuna `cmd` veya `powershell` yazarak terminali başlatın ya da mevcut terminal üzerinden proje klasörüne geçin.
3. Derleme betiğini çalıştırın.
4. Oluşturulan EXE dosyasını `dist` klasöründe bulabilirsiniz.

### 4. Uygulamayı Çalıştırma

Derleme başarıyla tamamlandıktan sonra uygulamayı çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```cmd
dist\DDS2PNG.exe
```

Alternatif olarak `dist` klasörüne giderek `DDS2PNG.exe` dosyasına çift tıklayabilirsiniz.

**Not:** Uygulamayı çalıştırmak için CMD veya PowerShell'i yönetici olarak açmanız gerekmez.

## Geliştirici

**vectordevworks**

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için proje deposundaki `LICENSE` dosyasına bakın.
