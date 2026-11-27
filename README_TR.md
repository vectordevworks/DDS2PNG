<div align="center">

# DDS2PNG

### DDS'den PNG'ye Dönüştürücü

DDS (DirectDraw Surface) biçimindeki doku dosyalarını kolayca PNG formatına dönüştürün.

Python tabanlı, hafif ve kullanımı kolay masaüstü uygulaması.

<p> <a href="[https://github.com/vectordevworks/DDS2PNG](https://github.com/vectordevworks/DDS2PNG)"> <img src="[https://img.shields.io/badge/GitHub-Kaynak%20Kod-181717?style=for-the-badge&logo=github](https://img.shields.io/badge/GitHub-Kaynak%20Kod-181717?style=for-the-badge&logo=github)" alt="GitHub"> </a> <a href="[https://github.com/vectordevworks/DDS2PNG/issues](https://github.com/vectordevworks/DDS2PNG/issues)"> <img src="[https://img.shields.io/badge/Hata%20Bildir-Issues-red?style=for-the-badge&logo=github](https://img.shields.io/badge/Hata%20Bildir-Issues-red?style=for-the-badge&logo=github)" alt="Issues"> </a> <a href="LICENSE"> <img src="[https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge](https://img.shields.io/badge/Lisans-MIT-green?style=for-the-badge)" alt="MIT License"> </a> </p>

<p> <img src="[https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)" alt="Python"> <img src="[https://img.shields.io/badge/Platform-Windows-blue?style=flat-square&logo=windows&logoColor=white](https://img.shields.io/badge/Platform-Windows-blue?style=flat-square&logo=windows&logoColor=white)" alt="Windows"> <img src="[https://img.shields.io/badge/Format-DDS%20%E2%86%92%20PNG-orange?style=flat-square](https://img.shields.io/badge/Format-DDS%20%E2%86%92%20PNG-orange?style=flat-square)" alt="DDS to PNG"> </p>

---

### 🌐 Dil Seçimi

<a href="README.md"><img src="[https://flagcdn.com/gb.svg](https://flagcdn.com/gb.svg)" width="20" alt="English"> English</a> |  
<a href="README_DE.md"><img src="[https://flagcdn.com/de.svg](https://flagcdn.com/de.svg)" width="20" alt="Deutsch"> Deutsch</a> |  
<a href="README_ES.md"><img src="[https://flagcdn.com/es.svg](https://flagcdn.com/es.svg)" width="20" alt="Español"> Español</a> |  
<a href="README_FR.md"><img src="[https://flagcdn.com/fr.svg](https://flagcdn.com/fr.svg)" width="20" alt="Français"> Français</a> |  
<a href="README_JA.md"><img src="[https://flagcdn.com/jp.svg](https://flagcdn.com/jp.svg)" width="20" alt="日本語"> 日本語</a> |  
<a href="README_KO.md"><img src="[https://flagcdn.com/kr.svg](https://flagcdn.com/kr.svg)" width="20" alt="한국어"> 한국어</a> |  
<a href="README_PT.md"><img src="[https://flagcdn.com/pt.svg](https://flagcdn.com/pt.svg)" width="20" alt="Português"> Português</a> |  
<a href="README_RU.md"><img src="[https://flagcdn.com/ru.svg](https://flagcdn.com/ru.svg)" width="20" alt="Русский"> Русский</a> |  
<a href="README_ZH_CN.md"><img src="[https://flagcdn.com/cn.svg](https://flagcdn.com/cn.svg)" width="20" alt="简体中文"> 简体中文</a> |  
<strong><img src="[https://flagcdn.com/tr.svg](https://flagcdn.com/tr.svg)" width="20" alt="Türkçe"> Türkçe</strong>

---

### 📑 İçindekiler

<a href="#genel-bakis">🔍 Genel Bakış</a> |  
<a href="#ozellikler">✨ Özellikler</a> |  
<a href="#gereksinimler">📋 Gereksinimler</a> |  
<a href="#kurulum">📥 Kurulum</a> |  
<a href="#sanal-ortam-istege-bagli">🐍 Sanal Ortam</a> |  
<a href="#kullanim">🚀 Kullanım</a> |  
<a href="#derleme-exe-olusturma">📦 Derleme (EXE)</a> |  
<a href="#gelistirici">👨‍💻 Geliştirici</a> |  
<a href="#lisans">📄 Lisans</a>

</div>

---

## 🔍 Genel Bakış

**DDS2PNG**, DDS (DirectDraw Surface) biçimindeki doku dosyalarını PNG formatına dönüştürmenizi sağlayan, Python tabanlı hafif bir masaüstü uygulamasıdır.

Basit grafik arayüzü sayesinde dosyalarınızı kolayca seçebilir ve dönüştürme işlemini gerçekleştirebilirsiniz. Komut satırı komutlarıyla uğraşmanız gerekmez.

Dönüştürme işlemleri Microsoft DirectXTex (Texconv) aracılığıyla gerçekleştirilir.

Texconv aracı uygulamayla birlikte `assets` klasöründe sunulur.

## ✨ Özellikler

- **DDS'den PNG'ye dönüştürme:** DDS dosyalarını PNG formatına dönüştürür.
    
- **Grafik arayüz:** Dosya seçme ve dönüştürme işlemlerini kolaylaştıran basit bir arayüz sunar.
    
- **Texconv desteği:** DDS dosyalarının dönüştürülmesi için Microsoft DirectXTex aracını kullanır.
    
- **Kolay kullanım:** Dönüştürme işlemini komut satırı kullanmadan gerçekleştirmenizi sağlar.
    

## 📋 Gereksinimler

- Windows
    
- Python 3.x
    
- Pillow
    
- Microsoft DirectXTex (Texconv)
    

`tkinter`, `ctypes`, `json`, `math`, `os` ve `pathlib` modülleri Python standart kütüphanesinin bir parçasıdır.

Texconv, DDS dosyalarını PNG formatına dönüştürmek için kullanılır ve uygulamayla birlikte `assets` klasöründe sunulur.

### Texconv (İsteğe Bağlı İndirme)

Projeyle birlikte sunulan Texconv çalışmazsa veya manuel olarak indirmek isterseniz aşağıdaki yöntemleri kullanabilirsiniz.

**PowerShell (Winget):**

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Kurulumu kontrol etmek için:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Manuel İndirme:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## 📥 Kurulum

1. Depoyu klonlayın:
    

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Proje klasörünü açın.
    
3. PowerShell'i proje klasöründe başlatın.
    
4. Gerekli Python paketlerini yükleyin:
    

```
py -m pip install -r requirements.txt
```

## 🐍 Sanal Ortam (İsteğe Bağlı)

Python bağımlılıklarını diğer projelerden ayrı tutmak için sanal ortam kullanabilirsiniz.

**1. Sanal ortam oluşturun:**

```
py -m venv .venv
```

**2. Sanal ortamı etkinleştirin:**

```
.\.venv\Scripts\Activate.ps1
```

**3. Gerekli bağımlılıkları yükleyin:**

```
py -m pip install -r requirements.txt
```

**4. İşiniz bittiğinde sanal ortamı devre dışı bırakın:**

```
deactivate
```

**CMD (Komut İstemi) üzerinden etkinleştirme:**

PowerShell yerine CMD kullanıyorsanız:

```
.venv\Scripts\activate.bat
```

Sanal ortamdan çıkmak için:

```
deactivate
```

### Sanal Ortam Etkinleştirme Sorunları

Bazı durumlarda PowerShell, güvenlik ilkesi (Execution Policy) nedeniyle sanal ortamı etkinleştirmeyi engelleyebilir.

Bu durumda aşağıdaki komutu çalıştırabilirsiniz:

```
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Ardından sanal ortamı tekrar etkinleştirin:

```
.\.venv\Scripts\Activate.ps1
```

Bu ayar yalnızca açık olan PowerShell oturumu için geçerlidir. Yeni bir PowerShell oturumu açıldığında varsayılan ayarlar yeniden uygulanır.

### Sanal Ortamı Etkinleştirmeden Kullanma

Sanal ortamı etkinleştirmek zorunlu değildir. Etkinleştirme işlemi başarısız olursa Python ve pip dosyalarını doğrudan çağırarak sanal ortamı kullanmaya devam edebilirsiniz.

**Bağımlılıkları yüklemek için:**

```
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

**Uygulamayı çalıştırmak için:**

```
.\.venv\Scripts\python.exe DDSConverter.pyw
```

**Not:** Sanal ortam oluşturma, etkinleştirme, bağımlılıkları yükleme ve devre dışı bırakma işlemleri için yönetici izni gerekmez. Ancak Python'un doğru şekilde kurulu olması ve gerekli dosyalara erişim izninizin bulunması gerekir.

## 🚀 Kullanım

1. `DDSConverter.pyw` dosyasını çalıştırın:
    

```
pyw .\DDSConverter.pyw
```

Alternatif olarak:

```
pythonw .\DDSConverter.pyw
```

2. Dönüştürmek istediğiniz DDS dosyasını seçin.
    
3. Çıktı klasörü olarak mevcut `convert` klasörünü seçebilir veya dilediğiniz klasörü belirleyebilirsiniz.
    
4. PNG formatına dönüştürme işlemini gerçekleştirin.
    

## 📦 Derleme (EXE Oluşturma)

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

```
cd /d "PROJE_KLASORUNUN_YOLU"
```

**PowerShell:**

```
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

```
powershell -ExecutionPolicy Bypass -File "scripts\buid.ps1"
```

**PowerShell üzerinden çalıştırma:**

```
.\scripts\buid.ps1
```

### 3. Derleme Çıktısı

Derleme başarıyla tamamlandığında EXE dosyası aşağıdaki konumda oluşturulur:

```
dist\DDS2PNG.exe
```

**Yeni bir sürüm derlemek için izlenecek adımlar:**

1. DDS2PNG proje klasörünü açın.
    
2. Adres çubuğuna `cmd` veya `powershell` yazarak terminali başlatın ya da mevcut terminal üzerinden proje klasörüne geçin.
    
3. Derleme betiğini çalıştırın.
    
4. Oluşturulan EXE dosyasını `dist` klasöründe bulabilirsiniz.
    

### 4. Uygulamayı Çalıştırma

Derleme başarıyla tamamlandıktan sonra uygulamayı çalıştırmak için aşağıdaki komutu kullanabilirsiniz:

```
dist\DDS2PNG.exe
```

Alternatif olarak `dist` klasörüne giderek `DDS2PNG.exe` dosyasına çift tıklayabilirsiniz.

**Not:** Uygulamayı çalıştırmak için CMD veya PowerShell'i yönetici olarak açmanız gerekmez.

## 👨‍💻 Geliştirici

<div align="center">

**VectorDevWorks**

<a href="[https://github.com/vectordevworks](https://github.com/vectordevworks)"> <img src="[https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github](https://img.shields.io/badge/GitHub-VectorDevWorks-181717?style=for-the-badge&logo=github)" alt="VectorDevWorks GitHub"> </a>

</div>

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için proje deposundaki `LICENSE` dosyasına bakın.

---

<div align="center">

**VectorDevWorks tarafından geliştirilmiştir.**

⭐ Projeyi beğendiyseniz GitHub üzerinden yıldız vermeyi unutmayın!

<a href="[https://github.com/vectordevworks/DDS2PNG](https://github.com/vectordevworks/DDS2PNG)"> <img src="[https://img.shields.io/badge/Proje%20Deposu-DDS2PNG-blue?style=for-the-badge&logo=github](https://img.shields.io/badge/Proje%20Deposu-DDS2PNG-blue?style=for-the-badge&logo=github)" alt="DDS2PNG Repository"> </a>

</div>
