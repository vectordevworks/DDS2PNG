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

DDS'den PNG'ye Dönüştürücü, DDS (DirectDraw Surface) biçimindeki doku dosyalarını PNG görüntülerine dönüştürmenizi sağlayan, Python tabanlı hafif bir masaüstü uygulamasıdır. Basit grafik arayüzü sayesinde dosyalarınızı kolayca seçebilir ve dönüştürme işlemini gerçekleştirebilirsiniz.

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

```
winget install --id Microsoft.DirectXTex.Texconv --exact
```

Kurulumu kontrol etmek için:

```
winget list --id Microsoft.DirectXTex.Texconv
```

**Manuel İndirme:**

[Microsoft DirectXTex Releases](https://github.com/microsoft/DirectXTex/releases)

## Kurulum

1. Depoyu klonlayın:
    

```
git clone https://github.com/vectordevworks/DDS2PNG.git
```

2. Proje klasörünü açın.
    
3. PowerShell'i bu klasörde başlatın.
    
4. Gerekli Python paketlerini yükleyin:
    

```
py -m pip install -r requirements.txt
```

## Sanal Ortam (İsteğe Bağlı)

Python bağımlılıklarını diğer projelerden ayrı tutmak için sanal ortam kullanabilirsiniz:

1. Sanal ortam oluşturun:
    

```
py -m venv .venv
```

2. Sanal ortamı etkinleştirin:
    

```
.\.venv\Scripts\Activate.ps1
```

3. Gerekli bağımlılıkları yükleyin:
    

```
py -m pip install -r requirements.txt
```

4. İşiniz bittiğinde sanal ortamı devre dışı bırakın:
    

```
deactivate
```

## Kullanım

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

## Derleme (EXE Oluşturma)

Python uygulamasını tek bir EXE dosyasına dönüştürmek için PyInstaller kullanılır.

### 1. Proje Klasörüne Geçiş

PowerShell'i proje klasöründe açın.

### 2. İkon ve Dil Görsellerini Gömme

Aşağıdaki komutu çalıştırarak `embed_icon.ps1` betiğini başlatın. Bu betik, uygulama simgesini ve dil seçimi için kullanılan PNG görsellerini Python dosyasına gömer.

```
powershell.exe -NoProfile -ExecutionPolicy Bypass -File ".\scripts\embed_icon.ps1"
```

**Not:** `-ExecutionPolicy Bypass` parametresi, Windows'un yürütme ilkesi nedeniyle PowerShell betiklerinin çalıştırılmasını engelleyebildiği durumlarda kullanılır. Bu parametre yalnızca başlatılan PowerShell işlemi için geçerlidir ve sistem genelindeki güvenlik ayarlarını değiştirmez.
### 3. Derleme Çıktısı

Derleme başarıyla tamamlandığında EXE dosyası aşağıdaki konumda oluşturulur:

```
dist\DDS2PNG.exe
```

**Yeni bir sürüm derlemek için izlenecek adımlar:**

1. PowerShell'i açın.
    
2. PyInstaller'ın kurulu olduğundan emin olun.
    
3. Proje klasörüne geçin.
    
4. Derleme betiğini çalıştırın.
    
5. Oluşturulan EXE dosyasını `dist` klasöründe bulabilirsiniz.
    

## Geliştirici

**vectordevworks**

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Ayrıntılar için proje deposundaki `LICENSE` dosyasına bakın.