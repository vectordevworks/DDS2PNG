
# -*- coding: utf-8 -*-

from pathlib import Path
import sys
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import font as tkfont

import math
import ctypes
import json
import threading
import queue
import subprocess
import shutil


# ============================================================
# APPLICATION SETTINGS
# ============================================================

LANGUAGES = {
    "tr": "Türkçe",
    "en": "English",
    "de": "Deutsch",
    "fr": "Français",
    "es": "Español",
    "pt": "Português",
    "ru": "Русский",
    "ja": "日本語",
    "zh-CN": "简体中文",
    "ko": "한국어"
}

APP_NAMES = {
    "tr": "DDS'den PNG'ye Dönüştürücü",
    "en": "DDS to PNG Converter",
    "de": "DDS-zu-PNG-Konverter",
    "fr": "Convertisseur DDS vers PNG",
    "es": "Convertidor de DDS a PNG",
    "pt": "Conversor de DDS para PNG",
    "ru": "Конвертер DDS в PNG",
    "ja": "DDSからPNGへのコンバーター",
    "zh-CN": "DDS 转 PNG 转换器",
    "ko": "DDS-PNG 변환기"
}

VERSION = "1.0"
DEVELOPER = "vectordevworks"


# ============================================================
# RESOURCE PATH (PYINSTALLER COMPATIBILITY)
# ============================================================

def resource_path(relative_path):

    """
    Returns the correct resource path for both
    normal Python execution and PyInstaller builds.
    """

    if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):

        base_path = Path(sys._MEIPASS)

    else:

        base_path = Path(__file__).resolve().parent

    return base_path / relative_path


APP_DIR = Path(__file__).resolve().parent

ASSETS_DIR = resource_path("assets")

ICON_PATH = ASSETS_DIR / "icon.ico"
LANGUAGE_ICON_PATH = ASSETS_DIR / "language.png"

TEXCONV_LOCAL_PATH = resource_path("texconv.exe")


# ============================================================
# CONFIGURATION
# ============================================================

CONFIG_DIR = (
    Path.home()
    / ".vectordevworks"
    / "dds_to_png_converter"
)

CONFIG_FILE = CONFIG_DIR / "config.json"


# ============================================================
# TRANSLATIONS
# ============================================================

EN = {
    "Dosya": "File",
    "Araçlar": "Tools",
    "Yardım": "Help",
    "Dil": "Language",
    "Türkçe": "Turkish",
    "English": "English",

    "DDS Dosyası Ekle": "Add DDS Files",
    "Çıktı Klasörü Seç": "Select Output Folder",
    "Listeyi Temizle": "Clear List",
    "Çıkış": "Exit",
    "Seçilenleri Kaldır": "Remove Selected",
    "Seçilenleri Dönüştür": "Convert Selected",
    "Tümünü Dönüştür": "Convert All",
    "Hakkında": "About",

    "Doku Dönüştürme Stüdyosu": "Texture Conversion Studio",
    "Hazır": "Ready",
    "DÖNÜŞTÜRME İLERLEMESİ": "CONVERSION PROGRESS",
    "Bekleniyor...": "Waiting...",
    "DOSYA LİSTESİ": "FILE LIST",
    "Dosya Adı": "File Name",
    "Dosya Konumu": "File Location",
    "Durum": "Status",
    "dosya": "files",
    "+ Dosya Ekle": "+ Add Files",

    "ÇIKTI KLASÖRÜ": "OUTPUT FOLDER",
    "Kaynak dosyaların bulunduğu klasör":
        "Folder containing source files",
    "Klasör Seç": "Browse",

    "Bekleniyor": "Waiting",
    "Tamamlandı": "Completed",
    "Hata": "Error",

    "DDS Dosyalarını Seç": "Select DDS Files",
    "DDS Dosyaları": "DDS Files",
    "Tüm Dosyalar": "All Files",
    "Çıktı Klasörünü Seç": "Select Output Folder",

    "Dosya Seçilmedi": "No File Selected",
    "Lütfen dönüştürmek istediğiniz dosyaları seçin.":
        "Please select the files you want to convert.",

    "Dosya Bulunamadı": "No Files Found",
    "Önce DDS dosyası ekleyin.":
        "Please add DDS files first.",

    "yeni dosya eklendi.": "new file(s) added.",
    "Seçilen dosyalar kaldırıldı.":
        "Selected files removed.",
    "Dosya listesi temizlendi.":
        "File list cleared.",
    "Çıktı klasörü güncellendi.":
        "Output folder updated.",

    "Dönüştürülüyor:": "Converting:",
    "İşlem ilerlemesi:": "Progress:",
    "Tamamlandı:": "Completed:",
    "Hatalı:": "Failed:",

    "Dönüştürme tamamlandı. Başarılı:":
        "Conversion finished. Successful:",

    "İşlem Tamamlandı": "Operation Completed",
    "Dönüştürme işlemi tamamlandı.":
        "The conversion process has finished.",

    "Başarılı:": "Successful:",
    "Hatalı:": "Failed:",

    "SÜRÜM": "VERSION",
    "Sürüm:": "Version:",
    "Geliştirici:": "Developer:",

    "DDS dosyalarını PNG formatına dönüştürür.":
        "Converts DDS files to PNG format.",

    "Python ve DirectXTex tarafından desteklenmektedir.":
        "Powered by Python and DirectXTex.",

    "Aynı isimli dosya var":
        "A file with the same name already exists",

    "Dosya zaten mevcut:":
        "File already exists:",

    "Üzerine yazılsın mı?":
        "Do you want to overwrite it?",

    "Dönüştürme sırasında çıkış yapılamaz.":
        "Cannot exit during conversion.",

    "Texconv bulunamadı":
        "Texconv not found",

    "Texconv dosyası bulunamadı.":
        "Texconv executable was not found.",

    "texconv.exe dosyasını programın bulunduğu klasöre koyun.":
        "Place texconv.exe in the application folder.",

    "Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.":
        "Conversion tool not found. Please check texconv.exe.",

    "Texconv dönüştürme hatası":
        "Texconv conversion error"
}

# Additional translations. Any missing entry falls back to English.
TRANSLATIONS = {
    "tr": {},
    "en": EN,
    "de": {
        'Dosya': 'Datei',
        'Araçlar': 'Werkzeuge',
        'Yardım': 'Hilfe',
        'Dil': 'Sprache',
        'Türkçe': 'Türkisch',
        'English': 'Englisch',
        'DDS Dosyası Ekle': 'DDS-Dateien hinzufügen',
        'Çıktı Klasörü Seç': 'Ausgabeordner auswählen',
        'Listeyi Temizle': 'Liste leeren',
        'Çıkış': 'Beenden',
        'Seçilenleri Kaldır': 'Auswahl entfernen',
        'Seçilenleri Dönüştür': 'Auswahl konvertieren',
        'Tümünü Dönüştür': 'Alle konvertieren',
        'Hakkında': 'Info',
        'Doku Dönüştürme Stüdyosu': 'Textur-Konvertierungsstudio',
        'Hazır': 'Bereit',
        'DÖNÜŞTÜRME İLERLEMESİ': 'KONVERTIERUNGSFORTSCHRITT',
        'Bekleniyor...': 'Wartet...',
        'DOSYA LİSTESİ': 'DATEILISTE',
        'Dosya Adı': 'Dateiname',
        'Dosya Konumu': 'Dateipfad',
        'Durum': 'Status',
        'dosya': 'Dateien',
        '+ Dosya Ekle': '+ Dateien hinzufügen',
        'ÇIKTI KLASÖRÜ': 'AUSGABEORDNER',
        'Kaynak dosyaların bulunduğu klasör': 'Ordner mit Quelldateien',
        'Klasör Seç': 'Durchsuchen',
        'Bekleniyor': 'Ausstehend',
        'Tamamlandı': 'Abgeschlossen',
        'Hata': 'Fehler',
        'DDS Dosyalarını Seç': 'DDS-Dateien auswählen',
        'DDS Dosyaları': 'DDS-Dateien',
        'Tüm Dosyalar': 'Alle Dateien',
        'Çıktı Klasörünü Seç': 'Ausgabeordner auswählen',
        'Dosya Seçilmedi': 'Keine Datei ausgewählt',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': 'Bitte wählen Sie die zu konvertierenden Dateien aus.',
        'Dosya Bulunamadı': 'Keine Dateien gefunden',
        'Önce DDS dosyası ekleyin.': 'Fügen Sie zuerst DDS-Dateien hinzu.',
        'yeni dosya eklendi.': 'neue Datei(en) hinzugefügt.',
        'Seçilen dosyalar kaldırıldı.': 'Ausgewählte Dateien entfernt.',
        'Dosya listesi temizlendi.': 'Dateiliste geleert.',
        'Çıktı klasörü güncellendi.': 'Ausgabeordner aktualisiert.',
        'Dönüştürülüyor:': 'Konvertierung:',
        'İşlem ilerlemesi:': 'Fortschritt:',
        'Tamamlandı:': 'Abgeschlossen:',
        'Hatalı:': 'Fehlgeschlagen:',
        'Dönüştürme tamamlandı. Başarılı:': 'Konvertierung abgeschlossen. Erfolgreich:',
        'İşlem Tamamlandı': 'Vorgang abgeschlossen',
        'Dönüştürme işlemi tamamlandı.': 'Die Konvertierung wurde abgeschlossen.',
        'Başarılı:': 'Erfolgreich:',
        'SÜRÜM': 'VERSION',
        'Sürüm:': 'Version:',
        'Geliştirici:': 'Entwickler:',
        'DDS dosyalarını PNG formatına dönüştürür.': 'Konvertiert DDS-Dateien in das PNG-Format.',
        'Python ve DirectXTex tarafından desteklenmektedir.': 'Unterstützt von Python und DirectXTex.',
        'Aynı isimli dosya var': 'Eine Datei mit diesem Namen ist bereits vorhanden',
        'Dosya zaten mevcut:': 'Datei bereits vorhanden:',
        'Üzerine yazılsın mı?': 'Möchten Sie sie überschreiben?',
        'Dönüştürme sırasında çıkış yapılamaz.': 'Während der Konvertierung ist das Beenden nicht möglich.',
        'Texconv bulunamadı': 'Texconv nicht gefunden',
        'Texconv dosyası bulunamadı.': 'Die Texconv-Datei wurde nicht gefunden.',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': 'Legen Sie texconv.exe im Anwendungsordner ab.',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': 'Konvertierungstool nicht gefunden. Bitte überprüfen Sie texconv.exe.',
        'Texconv dönüştürme hatası': 'Texconv-Konvertierungsfehler',
    },
    "fr": {
        'Dosya': 'Fichier',
        'Araçlar': 'Outils',
        'Yardım': 'Aide',
        'Dil': 'Langue',
        'Türkçe': 'Turc',
        'English': 'Anglais',
        'DDS Dosyası Ekle': 'Ajouter des fichiers DDS',
        'Çıktı Klasörü Seç': 'Choisir le dossier de sortie',
        'Listeyi Temizle': 'Vider la liste',
        'Çıkış': 'Quitter',
        'Seçilenleri Kaldır': 'Supprimer la sélection',
        'Seçilenleri Dönüştür': 'Convertir la sélection',
        'Tümünü Dönüştür': 'Tout convertir',
        'Hakkında': 'À propos',
        'Doku Dönüştürme Stüdyosu': 'Studio de conversion de textures',
        'Hazır': 'Prêt',
        'DÖNÜŞTÜRME İLERLEMESİ': 'PROGRESSION DE LA CONVERSION',
        'Bekleniyor...': 'En attente...',
        'DOSYA LİSTESİ': 'LISTE DES FICHIERS',
        'Dosya Adı': 'Nom du fichier',
        'Dosya Konumu': 'Emplacement du fichier',
        'Durum': 'État',
        'dosya': 'fichiers',
        '+ Dosya Ekle': '+ Ajouter des fichiers',
        'ÇIKTI KLASÖRÜ': 'DOSSIER DE SORTIE',
        'Kaynak dosyaların bulunduğu klasör': 'Dossier contenant les fichiers source',
        'Klasör Seç': 'Parcourir',
        'Bekleniyor': 'En attente',
        'Tamamlandı': 'Terminé',
        'Hata': 'Erreur',
        'DDS Dosyalarını Seç': 'Sélectionner des fichiers DDS',
        'DDS Dosyaları': 'Fichiers DDS',
        'Tüm Dosyalar': 'Tous les fichiers',
        'Çıktı Klasörünü Seç': 'Sélectionner le dossier de sortie',
        'Dosya Seçilmedi': 'Aucun fichier sélectionné',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': 'Veuillez sélectionner les fichiers à convertir.',
        'Dosya Bulunamadı': 'Aucun fichier trouvé',
        'Önce DDS dosyası ekleyin.': "Veuillez d'abord ajouter des fichiers DDS.",
        'yeni dosya eklendi.': 'nouveau(x) fichier(s) ajouté(s).',
        'Seçilen dosyalar kaldırıldı.': 'Fichiers sélectionnés supprimés.',
        'Dosya listesi temizlendi.': 'Liste des fichiers vidée.',
        'Çıktı klasörü güncellendi.': 'Dossier de sortie mis à jour.',
        'Dönüştürülüyor:': 'Conversion :',
        'İşlem ilerlemesi:': 'Progression :',
        'Tamamlandı:': 'Terminé :',
        'Hatalı:': 'Échec :',
        'Dönüştürme tamamlandı. Başarılı:': 'Conversion terminée. Réussites :',
        'İşlem Tamamlandı': 'Opération terminée',
        'Dönüştürme işlemi tamamlandı.': 'La conversion est terminée.',
        'Başarılı:': 'Réussite :',
        'SÜRÜM': 'VERSION',
        'Sürüm:': 'Version :',
        'Geliştirici:': 'Développeur :',
        'DDS dosyalarını PNG formatına dönüştürür.': 'Convertit les fichiers DDS au format PNG.',
        'Python ve DirectXTex tarafından desteklenmektedir.': 'Propulsé par Python et DirectXTex.',
        'Aynı isimli dosya var': 'Un fichier portant le même nom existe déjà',
        'Dosya zaten mevcut:': 'Le fichier existe déjà :',
        'Üzerine yazılsın mı?': 'Voulez-vous le remplacer ?',
        'Dönüştürme sırasında çıkış yapılamaz.': 'Impossible de quitter pendant la conversion.',
        'Texconv bulunamadı': 'Texconv introuvable',
        'Texconv dosyası bulunamadı.': 'L’exécutable Texconv est introuvable.',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': 'Placez texconv.exe dans le dossier de l’application.',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': 'Outil de conversion introuvable. Vérifiez texconv.exe.',
        'Texconv dönüştürme hatası': 'Erreur de conversion Texconv',
    },
    "es": {
        'Dosya': 'Archivo',
        'Araçlar': 'Herramientas',
        'Yardım': 'Ayuda',
        'Dil': 'Idioma',
        'Türkçe': 'Turco',
        'English': 'Inglés',
        'DDS Dosyası Ekle': 'Añadir archivos DDS',
        'Çıktı Klasörü Seç': 'Seleccionar carpeta de salida',
        'Listeyi Temizle': 'Vaciar lista',
        'Çıkış': 'Salir',
        'Seçilenleri Kaldır': 'Eliminar seleccionados',
        'Seçilenleri Dönüştür': 'Convertir seleccionados',
        'Tümünü Dönüştür': 'Convertir todo',
        'Hakkında': 'Acerca de',
        'Doku Dönüştürme Stüdyosu': 'Estudio de conversión de texturas',
        'Hazır': 'Listo',
        'DÖNÜŞTÜRME İLERLEMESİ': 'PROGRESO DE CONVERSIÓN',
        'Bekleniyor...': 'Esperando...',
        'DOSYA LİSTESİ': 'LISTA DE ARCHIVOS',
        'Dosya Adı': 'Nombre del archivo',
        'Dosya Konumu': 'Ubicación del archivo',
        'Durum': 'Estado',
        'dosya': 'archivos',
        '+ Dosya Ekle': '+ Añadir archivos',
        'ÇIKTI KLASÖRÜ': 'CARPETA DE SALIDA',
        'Kaynak dosyaların bulunduğu klasör': 'Carpeta que contiene los archivos de origen',
        'Klasör Seç': 'Examinar',
        'Bekleniyor': 'En espera',
        'Tamamlandı': 'Completado',
        'Hata': 'Error',
        'DDS Dosyalarını Seç': 'Seleccionar archivos DDS',
        'DDS Dosyaları': 'Archivos DDS',
        'Tüm Dosyalar': 'Todos los archivos',
        'Çıktı Klasörünü Seç': 'Seleccionar carpeta de salida',
        'Dosya Seçilmedi': 'No se seleccionó ningún archivo',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': 'Selecciona los archivos que deseas convertir.',
        'Dosya Bulunamadı': 'No se encontraron archivos',
        'Önce DDS dosyası ekleyin.': 'Añade primero archivos DDS.',
        'yeni dosya eklendi.': 'archivo(s) nuevo(s) añadido(s).',
        'Seçilen dosyalar kaldırıldı.': 'Archivos seleccionados eliminados.',
        'Dosya listesi temizlendi.': 'Lista de archivos vaciada.',
        'Çıktı klasörü güncellendi.': 'Carpeta de salida actualizada.',
        'Dönüştürülüyor:': 'Convirtiendo:',
        'İşlem ilerlemesi:': 'Progreso:',
        'Tamamlandı:': 'Completado:',
        'Hatalı:': 'Fallidos:',
        'Dönüştürme tamamlandı. Başarılı:': 'Conversión finalizada. Correctos:',
        'İşlem Tamamlandı': 'Operación completada',
        'Dönüştürme işlemi tamamlandı.': 'El proceso de conversión ha finalizado.',
        'Başarılı:': 'Correctos:',
        'SÜRÜM': 'VERSIÓN',
        'Sürüm:': 'Versión:',
        'Geliştirici:': 'Desarrollador:',
        'DDS dosyalarını PNG formatına dönüştürür.': 'Convierte archivos DDS al formato PNG.',
        'Python ve DirectXTex tarafından desteklenmektedir.': 'Desarrollado con Python y DirectXTex.',
        'Aynı isimli dosya var': 'Ya existe un archivo con el mismo nombre',
        'Dosya zaten mevcut:': 'El archivo ya existe:',
        'Üzerine yazılsın mı?': '¿Quieres sobrescribirlo?',
        'Dönüştürme sırasında çıkış yapılamaz.': 'No se puede salir durante la conversión.',
        'Texconv bulunamadı': 'No se encontró Texconv',
        'Texconv dosyası bulunamadı.': 'No se encontró el ejecutable de Texconv.',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': 'Coloca texconv.exe en la carpeta de la aplicación.',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': 'No se encontró la herramienta de conversión. Comprueba texconv.exe.',
        'Texconv dönüştürme hatası': 'Error de conversión de Texconv',
    },
    "pt": {
        'Dosya': 'Arquivo',
        'Araçlar': 'Ferramentas',
        'Yardım': 'Ajuda',
        'Dil': 'Idioma',
        'Türkçe': 'Turco',
        'English': 'Inglês',
        'DDS Dosyası Ekle': 'Adicionar arquivos DDS',
        'Çıktı Klasörü Seç': 'Selecionar pasta de saída',
        'Listeyi Temizle': 'Limpar lista',
        'Çıkış': 'Sair',
        'Seçilenleri Kaldır': 'Remover selecionados',
        'Seçilenleri Dönüştür': 'Converter selecionados',
        'Tümünü Dönüştür': 'Converter tudo',
        'Hakkında': 'Sobre',
        'Doku Dönüştürme Stüdyosu': 'Estúdio de conversão de texturas',
        'Hazır': 'Pronto',
        'DÖNÜŞTÜRME İLERLEMESİ': 'PROGRESSO DA CONVERSÃO',
        'Bekleniyor...': 'Aguardando...',
        'DOSYA LİSTESİ': 'LISTA DE ARQUIVOS',
        'Dosya Adı': 'Nome do arquivo',
        'Dosya Konumu': 'Local do arquivo',
        'Durum': 'Status',
        'dosya': 'arquivos',
        '+ Dosya Ekle': '+ Adicionar arquivos',
        'ÇIKTI KLASÖRÜ': 'PASTA DE SAÍDA',
        'Kaynak dosyaların bulunduğu klasör': 'Pasta que contém os arquivos de origem',
        'Klasör Seç': 'Procurar',
        'Bekleniyor': 'Aguardando',
        'Tamamlandı': 'Concluído',
        'Hata': 'Erro',
        'DDS Dosyalarını Seç': 'Selecionar arquivos DDS',
        'DDS Dosyaları': 'Arquivos DDS',
        'Tüm Dosyalar': 'Todos os arquivos',
        'Çıktı Klasörünü Seç': 'Selecionar pasta de saída',
        'Dosya Seçilmedi': 'Nenhum arquivo selecionado',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': 'Selecione os arquivos que deseja converter.',
        'Dosya Bulunamadı': 'Nenhum arquivo encontrado',
        'Önce DDS dosyası ekleyin.': 'Adicione arquivos DDS primeiro.',
        'yeni dosya eklendi.': 'novo(s) arquivo(s) adicionado(s).',
        'Seçilen dosyalar kaldırıldı.': 'Arquivos selecionados removidos.',
        'Dosya listesi temizlendi.': 'Lista de arquivos limpa.',
        'Çıktı klasörü güncellendi.': 'Pasta de saída atualizada.',
        'Dönüştürülüyor:': 'Convertendo:',
        'İşlem ilerlemesi:': 'Progresso:',
        'Tamamlandı:': 'Concluído:',
        'Hatalı:': 'Com falha:',
        'Dönüştürme tamamlandı. Başarılı:': 'Conversão concluída. Sucesso:',
        'İşlem Tamamlandı': 'Operação concluída',
        'Dönüştürme işlemi tamamlandı.': 'O processo de conversão foi concluído.',
        'Başarılı:': 'Sucesso:',
        'SÜRÜM': 'VERSÃO',
        'Sürüm:': 'Versão:',
        'Geliştirici:': 'Desenvolvedor:',
        'DDS dosyalarını PNG formatına dönüştürür.': 'Converte arquivos DDS para o formato PNG.',
        'Python ve DirectXTex tarafından desteklenmektedir.': 'Desenvolvido com Python e DirectXTex.',
        'Aynı isimli dosya var': 'Já existe um arquivo com o mesmo nome',
        'Dosya zaten mevcut:': 'Arquivo já existente:',
        'Üzerine yazılsın mı?': 'Deseja sobrescrevê-lo?',
        'Dönüştürme sırasında çıkış yapılamaz.': 'Não é possível sair durante a conversão.',
        'Texconv bulunamadı': 'Texconv não encontrado',
        'Texconv dosyası bulunamadı.': 'O executável Texconv não foi encontrado.',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': 'Coloque texconv.exe na pasta do aplicativo.',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': 'Ferramenta de conversão não encontrada. Verifique texconv.exe.',
        'Texconv dönüştürme hatası': 'Erro de conversão do Texconv',
    },
    "ru": {
        'Dosya': 'Файл',
        'Araçlar': 'Инструменты',
        'Yardım': 'Справка',
        'Dil': 'Язык',
        'Türkçe': 'Турецкий',
        'English': 'Английский',
        'DDS Dosyası Ekle': 'Добавить файлы DDS',
        'Çıktı Klasörü Seç': 'Выбрать папку вывода',
        'Listeyi Temizle': 'Очистить список',
        'Çıkış': 'Выход',
        'Seçilenleri Kaldır': 'Удалить выбранные',
        'Seçilenleri Dönüştür': 'Преобразовать выбранные',
        'Tümünü Dönüştür': 'Преобразовать все',
        'Hakkında': 'О программе',
        'Doku Dönüştürme Stüdyosu': 'Студия преобразования текстур',
        'Hazır': 'Готово',
        'DÖNÜŞTÜRME İLERLEMESİ': 'ХОД ПРЕОБРАЗОВАНИЯ',
        'Bekleniyor...': 'Ожидание...',
        'DOSYA LİSTESİ': 'СПИСОК ФАЙЛОВ',
        'Dosya Adı': 'Имя файла',
        'Dosya Konumu': 'Расположение файла',
        'Durum': 'Статус',
        'dosya': 'файлов',
        '+ Dosya Ekle': '+ Добавить файлы',
        'ÇIKTI KLASÖRÜ': 'ПАПКА ВЫВОДА',
        'Kaynak dosyaların bulunduğu klasör': 'Папка с исходными файлами',
        'Klasör Seç': 'Обзор',
        'Bekleniyor': 'Ожидание',
        'Tamamlandı': 'Завершено',
        'Hata': 'Ошибка',
        'DDS Dosyalarını Seç': 'Выберите файлы DDS',
        'DDS Dosyaları': 'Файлы DDS',
        'Tüm Dosyalar': 'Все файлы',
        'Çıktı Klasörünü Seç': 'Выберите папку вывода',
        'Dosya Seçilmedi': 'Файл не выбран',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': 'Выберите файлы для преобразования.',
        'Dosya Bulunamadı': 'Файлы не найдены',
        'Önce DDS dosyası ekleyin.': 'Сначала добавьте файлы DDS.',
        'yeni dosya eklendi.': 'новых файлов добавлено.',
        'Seçilen dosyalar kaldırıldı.': 'Выбранные файлы удалены.',
        'Dosya listesi temizlendi.': 'Список файлов очищен.',
        'Çıktı klasörü güncellendi.': 'Папка вывода обновлена.',
        'Dönüştürülüyor:': 'Преобразование:',
        'İşlem ilerlemesi:': 'Выполнение:',
        'Tamamlandı:': 'Завершено:',
        'Hatalı:': 'Ошибки:',
        'Dönüştürme tamamlandı. Başarılı:': 'Преобразование завершено. Успешно:',
        'İşlem Tamamlandı': 'Операция завершена',
        'Dönüştürme işlemi tamamlandı.': 'Преобразование завершено.',
        'Başarılı:': 'Успешно:',
        'SÜRÜM': 'ВЕРСИЯ',
        'Sürüm:': 'Версия:',
        'Geliştirici:': 'Разработчик:',
        'DDS dosyalarını PNG formatına dönüştürür.': 'Преобразует файлы DDS в формат PNG.',
        'Python ve DirectXTex tarafından desteklenmektedir.': 'Работает на базе Python и DirectXTex.',
        'Aynı isimli dosya var': 'Файл с таким именем уже существует',
        'Dosya zaten mevcut:': 'Файл уже существует:',
        'Üzerine yazılsın mı?': 'Перезаписать файл?',
        'Dönüştürme sırasında çıkış yapılamaz.': 'Нельзя выйти во время преобразования.',
        'Texconv bulunamadı': 'Texconv не найден',
        'Texconv dosyası bulunamadı.': 'Исполняемый файл Texconv не найден.',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': 'Поместите texconv.exe в папку приложения.',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': 'Средство преобразования не найдено. Проверьте texconv.exe.',
        'Texconv dönüştürme hatası': 'Ошибка преобразования Texconv',
    },
    "ja": {
        'Dosya': 'ファイル',
        'Araçlar': 'ツール',
        'Yardım': 'ヘルプ',
        'Dil': '言語',
        'Türkçe': 'トルコ語',
        'English': '英語',
        'DDS Dosyası Ekle': 'DDSファイルを追加',
        'Çıktı Klasörü Seç': '出力フォルダーを選択',
        'Listeyi Temizle': 'リストをクリア',
        'Çıkış': '終了',
        'Seçilenleri Kaldır': '選択項目を削除',
        'Seçilenleri Dönüştür': '選択項目を変換',
        'Tümünü Dönüştür': 'すべて変換',
        'Hakkında': 'バージョン情報',
        'Doku Dönüştürme Stüdyosu': 'テクスチャ変換スタジオ',
        'Hazır': '準備完了',
        'DÖNÜŞTÜRME İLERLEMESİ': '変換の進行状況',
        'Bekleniyor...': '待機中...',
        'DOSYA LİSTESİ': 'ファイル一覧',
        'Dosya Adı': 'ファイル名',
        'Dosya Konumu': 'ファイルの場所',
        'Durum': '状態',
        'dosya': 'ファイル',
        '+ Dosya Ekle': '+ ファイルを追加',
        'ÇIKTI KLASÖRÜ': '出力フォルダー',
        'Kaynak dosyaların bulunduğu klasör': 'ソースファイルを含むフォルダー',
        'Klasör Seç': '参照',
        'Bekleniyor': '待機中',
        'Tamamlandı': '完了',
        'Hata': 'エラー',
        'DDS Dosyalarını Seç': 'DDSファイルを選択',
        'DDS Dosyaları': 'DDSファイル',
        'Tüm Dosyalar': 'すべてのファイル',
        'Çıktı Klasörünü Seç': '出力フォルダーを選択',
        'Dosya Seçilmedi': 'ファイルが選択されていません',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': '変換するファイルを選択してください。',
        'Dosya Bulunamadı': 'ファイルが見つかりません',
        'Önce DDS dosyası ekleyin.': '先にDDSファイルを追加してください。',
        'yeni dosya eklendi.': '個の新しいファイルを追加しました。',
        'Seçilen dosyalar kaldırıldı.': '選択したファイルを削除しました。',
        'Dosya listesi temizlendi.': 'ファイル一覧をクリアしました。',
        'Çıktı klasörü güncellendi.': '出力フォルダーを更新しました。',
        'Dönüştürülüyor:': '変換中:',
        'İşlem ilerlemesi:': '進行状況:',
        'Tamamlandı:': '完了:',
        'Hatalı:': '失敗:',
        'Dönüştürme tamamlandı. Başarılı:': '変換完了。成功:',
        'İşlem Tamamlandı': '処理完了',
        'Dönüştürme işlemi tamamlandı.': '変換処理が完了しました。',
        'Başarılı:': '成功:',
        'SÜRÜM': 'バージョン',
        'Sürüm:': 'バージョン:',
        'Geliştirici:': '開発者:',
        'DDS dosyalarını PNG formatına dönüştürür.': 'DDSファイルをPNG形式に変換します。',
        'Python ve DirectXTex tarafından desteklenmektedir.': 'PythonとDirectXTexを使用しています。',
        'Aynı isimli dosya var': '同じ名前のファイルが既に存在します',
        'Dosya zaten mevcut:': 'ファイルは既に存在します:',
        'Üzerine yazılsın mı?': '上書きしますか？',
        'Dönüştürme sırasında çıkış yapılamaz.': '変換中は終了できません。',
        'Texconv bulunamadı': 'Texconvが見つかりません',
        'Texconv dosyası bulunamadı.': 'Texconv実行ファイルが見つかりません。',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': 'texconv.exeをアプリケーションフォルダーに配置してください。',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': '変換ツールが見つかりません。texconv.exeを確認してください。',
        'Texconv dönüştürme hatası': 'Texconv変換エラー',
    },
    "zh-CN": {
        'Dosya': '文件',
        'Araçlar': '工具',
        'Yardım': '帮助',
        'Dil': '语言',
        'Türkçe': '土耳其语',
        'English': '英语',
        'DDS Dosyası Ekle': '添加 DDS 文件',
        'Çıktı Klasörü Seç': '选择输出文件夹',
        'Listeyi Temizle': '清空列表',
        'Çıkış': '退出',
        'Seçilenleri Kaldır': '移除所选项',
        'Seçilenleri Dönüştür': '转换所选项',
        'Tümünü Dönüştür': '全部转换',
        'Hakkında': '关于',
        'Doku Dönüştürme Stüdyosu': '纹理转换工作室',
        'Hazır': '就绪',
        'DÖNÜŞTÜRME İLERLEMESİ': '转换进度',
        'Bekleniyor...': '等待中...',
        'DOSYA LİSTESİ': '文件列表',
        'Dosya Adı': '文件名',
        'Dosya Konumu': '文件位置',
        'Durum': '状态',
        'dosya': '个文件',
        '+ Dosya Ekle': '+ 添加文件',
        'ÇIKTI KLASÖRÜ': '输出文件夹',
        'Kaynak dosyaların bulunduğu klasör': '包含源文件的文件夹',
        'Klasör Seç': '浏览',
        'Bekleniyor': '等待中',
        'Tamamlandı': '已完成',
        'Hata': '错误',
        'DDS Dosyalarını Seç': '选择 DDS 文件',
        'DDS Dosyaları': 'DDS 文件',
        'Tüm Dosyalar': '所有文件',
        'Çıktı Klasörünü Seç': '选择输出文件夹',
        'Dosya Seçilmedi': '未选择文件',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': '请选择要转换的文件。',
        'Dosya Bulunamadı': '未找到文件',
        'Önce DDS dosyası ekleyin.': '请先添加 DDS 文件。',
        'yeni dosya eklendi.': '个新文件已添加。',
        'Seçilen dosyalar kaldırıldı.': '已移除所选文件。',
        'Dosya listesi temizlendi.': '文件列表已清空。',
        'Çıktı klasörü güncellendi.': '输出文件夹已更新。',
        'Dönüştürülüyor:': '正在转换：',
        'İşlem ilerlemesi:': '进度：',
        'Tamamlandı:': '已完成：',
        'Hatalı:': '失败：',
        'Dönüştürme tamamlandı. Başarılı:': '转换完成。成功：',
        'İşlem Tamamlandı': '操作完成',
        'Dönüştürme işlemi tamamlandı.': '转换过程已完成。',
        'Başarılı:': '成功：',
        'SÜRÜM': '版本',
        'Sürüm:': '版本：',
        'Geliştirici:': '开发者：',
        'DDS dosyalarını PNG formatına dönüştürür.': '将 DDS 文件转换为 PNG 格式。',
        'Python ve DirectXTex tarafından desteklenmektedir.': '由 Python 和 DirectXTex 提供支持。',
        'Aynı isimli dosya var': '已存在同名文件',
        'Dosya zaten mevcut:': '文件已存在：',
        'Üzerine yazılsın mı?': '是否覆盖？',
        'Dönüştürme sırasında çıkış yapılamaz.': '转换过程中无法退出。',
        'Texconv bulunamadı': '未找到 Texconv',
        'Texconv dosyası bulunamadı.': '未找到 Texconv 可执行文件。',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': '请将 texconv.exe 放在应用程序文件夹中。',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': '未找到转换工具。请检查 texconv.exe。',
        'Texconv dönüştürme hatası': 'Texconv 转换错误',
    },
    "ko": {
        'Dosya': '파일',
        'Araçlar': '도구',
        'Yardım': '도움말',
        'Dil': '언어',
        'Türkçe': '터키어',
        'English': '영어',
        'DDS Dosyası Ekle': 'DDS 파일 추가',
        'Çıktı Klasörü Seç': '출력 폴더 선택',
        'Listeyi Temizle': '목록 지우기',
        'Çıkış': '종료',
        'Seçilenleri Kaldır': '선택 항목 제거',
        'Seçilenleri Dönüştür': '선택 항목 변환',
        'Tümünü Dönüştür': '모두 변환',
        'Hakkında': '정보',
        'Doku Dönüştürme Stüdyosu': '텍스처 변환 스튜디오',
        'Hazır': '준비',
        'DÖNÜŞTÜRME İLERLEMESİ': '변환 진행률',
        'Bekleniyor...': '대기 중...',
        'DOSYA LİSTESİ': '파일 목록',
        'Dosya Adı': '파일 이름',
        'Dosya Konumu': '파일 위치',
        'Durum': '상태',
        'dosya': '개 파일',
        '+ Dosya Ekle': '+ 파일 추가',
        'ÇIKTI KLASÖRÜ': '출력 폴더',
        'Kaynak dosyaların bulunduğu klasör': '원본 파일이 있는 폴더',
        'Klasör Seç': '찾아보기',
        'Bekleniyor': '대기 중',
        'Tamamlandı': '완료',
        'Hata': '오류',
        'DDS Dosyalarını Seç': 'DDS 파일 선택',
        'DDS Dosyaları': 'DDS 파일',
        'Tüm Dosyalar': '모든 파일',
        'Çıktı Klasörünü Seç': '출력 폴더 선택',
        'Dosya Seçilmedi': '파일이 선택되지 않음',
        'Lütfen dönüştürmek istediğiniz dosyaları seçin.': '변환할 파일을 선택하세요.',
        'Dosya Bulunamadı': '파일을 찾을 수 없음',
        'Önce DDS dosyası ekleyin.': '먼저 DDS 파일을 추가하세요.',
        'yeni dosya eklendi.': '개의 새 파일이 추가되었습니다.',
        'Seçilen dosyalar kaldırıldı.': '선택한 파일을 제거했습니다.',
        'Dosya listesi temizlendi.': '파일 목록을 지웠습니다.',
        'Çıktı klasörü güncellendi.': '출력 폴더를 업데이트했습니다.',
        'Dönüştürülüyor:': '변환 중:',
        'İşlem ilerlemesi:': '진행률:',
        'Tamamlandı:': '완료:',
        'Hatalı:': '실패:',
        'Dönüştürme tamamlandı. Başarılı:': '변환 완료. 성공:',
        'İşlem Tamamlandı': '작업 완료',
        'Dönüştürme işlemi tamamlandı.': '변환 작업이 완료되었습니다.',
        'Başarılı:': '성공:',
        'SÜRÜM': '버전',
        'Sürüm:': '버전:',
        'Geliştirici:': '개발자:',
        'DDS dosyalarını PNG formatına dönüştürür.': 'DDS 파일을 PNG 형식으로 변환합니다.',
        'Python ve DirectXTex tarafından desteklenmektedir.': 'Python 및 DirectXTex 기반입니다.',
        'Aynı isimli dosya var': '같은 이름의 파일이 이미 있습니다',
        'Dosya zaten mevcut:': '파일이 이미 존재합니다:',
        'Üzerine yazılsın mı?': '덮어쓰시겠습니까?',
        'Dönüştürme sırasında çıkış yapılamaz.': '변환 중에는 종료할 수 없습니다.',
        'Texconv bulunamadı': 'Texconv를 찾을 수 없음',
        'Texconv dosyası bulunamadı.': 'Texconv 실행 파일을 찾을 수 없습니다.',
        'texconv.exe dosyasını programın bulunduğu klasöre koyun.': 'texconv.exe를 프로그램 폴더에 넣으세요.',
        'Dönüştürme aracı bulunamadı. Lütfen texconv.exe dosyasını kontrol edin.': '변환 도구를 찾을 수 없습니다. texconv.exe를 확인하세요.',
        'Texconv dönüştürme hatası': 'Texconv 변환 오류',
    },
}


# ============================================================
# MIDNIGHT PRO COLORS
# ============================================================

BG = "#0D1220"
PANEL = "#151E32"
CARD = "#19243A"
CARD_HOVER = "#202E49"

ACCENT = "#4776C8"
ACCENT_HOVER = "#5A8BE0"

PURPLE = "#6550A8"
PURPLE_HOVER = "#7964C2"

TEXT = "#E8EFFB"
MUTED = "#8EA5C9"
BORDER = "#293750"

SUCCESS = "#56C99A"
ERROR = "#F07883"

LANGUAGE_BLUE = "#70B7FF"


# ============================================================
# WINDOWS TITLEBAR THEME
# ============================================================

def apply_titlebar_theme(root):

    try:
        dwmapi = ctypes.windll.dwmapi
        user32 = ctypes.windll.user32

        hwnd = user32.GetAncestor(
            root.winfo_id(),
            2
        )

        def set_attribute(attribute, value):

            return dwmapi.DwmSetWindowAttribute(
                hwnd,
                attribute,
                ctypes.byref(value),
                ctypes.sizeof(value)
            )

        dark_mode = ctypes.c_int(1)

        result = set_attribute(
            20,
            dark_mode
        )

        if result != 0:
            set_attribute(19, dark_mode)

        def set_color(attribute, color):

            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)

            color_value = ctypes.c_uint(
                r | (g << 8) | (b << 16)
            )

            set_attribute(
                attribute,
                color_value
            )

        set_color(35, BG)
        set_color(36, TEXT)
        set_color(34, BORDER)

    except Exception:
        pass


# ============================================================
# ROUNDED BUTTON
# ============================================================

class RoundedButton(tk.Canvas):

    def __init__(
        self,
        parent,
        text,
        command,
        color,
        hover_color,
        text_color="#FFFFFF",
        font=("Segoe UI", 9, "bold"),
        padx=18,
        height=42,
        radius=12
    ):

        self.button_text = text
        self.command = command

        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color

        self.button_font = tkfont.Font(
            family=font[0],
            size=font[1],
            weight=font[2] if len(font) > 2 else "normal"
        )

        self.height = height
        self.radius = radius

        width = (
            self.button_font.measure(text)
            + padx * 2
        )

        super().__init__(
            parent,
            width=width,
            height=height,
            bg=parent.cget("bg"),
            highlightthickness=0,
            bd=0,
            cursor="hand2"
        )

        self.enabled = True
        self.current_color = color

        self.draw_button()

        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.bind("<Button-1>", self.on_click)

    def rounded_rectangle(
        self,
        x1,
        y1,
        x2,
        y2,
        radius,
        **kwargs
    ):

        points = []

        corners = [
            (x1 + radius, y1 + radius, 180, 270),
            (x2 - radius, y1 + radius, 270, 360),
            (x2 - radius, y2 - radius, 0, 90),
            (x1 + radius, y2 - radius, 90, 180)
        ]

        for cx, cy, start, end in corners:

            for angle in range(start, end + 1, 10):

                rad = math.radians(angle)

                points.append(
                    (
                        cx + radius * math.cos(rad),
                        cy + radius * math.sin(rad)
                    )
                )

        return self.create_polygon(
            points,
            smooth=True,
            splinesteps=24,
            **kwargs
        )

    def draw_button(self):

        self.delete("all")

        self.rounded_rectangle(
            1,
            1,
            int(self["width"]) - 1,
            self.height - 1,
            self.radius,
            fill=self.current_color,
            outline=""
        )

        self.create_text(
            int(self["width"]) // 2,
            self.height // 2,
            text=self.button_text,
            fill=self.text_color,
            font=self.button_font
        )

    def on_enter(self, event=None):

        if not self.enabled:
            return

        self.current_color = self.hover_color
        self.draw_button()

    def on_leave(self, event=None):

        if not self.enabled:
            return

        self.current_color = self.color
        self.draw_button()

    def on_click(self, event=None):

        if self.enabled and self.command:
            self.command()

    def config(self, **kwargs):

        state = kwargs.pop("state", None)

        if state is not None:

            self.enabled = state != "disabled"

            if self.enabled:

                self.current_color = self.color
                super().config(cursor="hand2")

            else:

                self.current_color = "#30394D"
                super().config(cursor="arrow")

            self.draw_button()

        if kwargs:
            super().config(**kwargs)

    configure = config


# ============================================================
# MAIN APPLICATION
# ============================================================

class DDSConverter:

    def __init__(self, root):

        self.root = root

        self.root.geometry("920x680")
        self.root.minsize(780, 570)
        self.root.configure(bg=BG)

        # ----------------------------------------------------
        # APPLICATION ICON
        # ----------------------------------------------------

        try:

            if ICON_PATH.is_file():

                self.root.iconbitmap(
                    default=str(ICON_PATH)
                )

        except (tk.TclError, OSError) as error:

            print(
                f"Application icon loading error: {error}"
            )

        self.files = []
        self.file_status = {}

        self.output_dir = None

        self.is_converting = False
        self.is_closing = False

        self.active_menu = None
        self.active_menu_button = None

        self.menu_buttons = []
        self.menu_trigger_widgets = []

        self.conversion_queue = queue.Queue()

        # Keep PNG reference alive.
        self.language_icon = None

        self.language = self.load_language()

        # Set application name after loading language.
        self.root.title(self.get_app_name())

        self.setup_style()

        self.create_menu()
        self.create_interface()

        self.root.update_idletasks()

        apply_titlebar_theme(self.root)

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.on_close
        )

        self.root.bind(
            "<Control-o>",
            lambda event: self.add_files()
        )

        self.root.bind(
            "<Delete>",
            lambda event: self.remove_selected()
        )

        self.root.bind(
            "<Control-l>",
            lambda event: self.clear_files()
        )

        self.root.bind_all(
            "<Button-1>",
            self._dismiss_menu_on_outside_click,
            add="+"
        )

    # ========================================================
    # APPLICATION NAME
    # ========================================================

    def get_app_name(self):

        return APP_NAMES.get(
            self.language,
            APP_NAMES["tr"]
        )

    # ========================================================
    # TEXCONV
    # ========================================================

    def find_texconv(self):

        if TEXCONV_LOCAL_PATH.is_file():
            return str(TEXCONV_LOCAL_PATH)

        path = shutil.which("texconv.exe")

        if path:
            return path

        path = shutil.which("texconv")

        if path:
            return path

        return None

    def check_texconv(self):

        texconv = self.find_texconv()

        if texconv:
            return texconv

        messagebox.showerror(
            self.tr("Texconv bulunamadı"),
            (
                f"{self.tr('Texconv dosyası bulunamadı.')}\n\n"
                f"{self.tr('texconv.exe dosyasını programın bulunduğu klasöre koyun.')}"
            ),
            parent=self.root
        )

        return None

    # ========================================================
    # LANGUAGE SETTINGS
    # ========================================================

    def load_language(self):

        try:

            if CONFIG_FILE.exists():

                with CONFIG_FILE.open(
                    "r",
                    encoding="utf-8"
                ) as file:

                    config = json.load(file)

                language = config.get(
                    "language",
                    "tr"
                )

                if language in LANGUAGES:
                    return language

        except (OSError, ValueError, TypeError):
            pass

        return "tr"

    def save_language(self):

        try:

            CONFIG_DIR.mkdir(
                parents=True,
                exist_ok=True
            )

            config = {
                "language": self.language
            }

            with CONFIG_FILE.open(
                "w",
                encoding="utf-8"
            ) as file:

                json.dump(
                    config,
                    file,
                    ensure_ascii=False,
                    indent=4
                )

        except (OSError, TypeError) as error:

            print(
                f"Language saving error: {error}"
            )

    def tr(self, text):

        if self.language == "tr":
            return text

        language_translations = TRANSLATIONS.get(
            self.language,
            EN
        )

        return language_translations.get(
            text,
            EN.get(text, text)
        )

    def translate_runtime_text(self, text):

        """
        Translate text that was already displayed before a language change.

        The previous implementation only searched for English source strings.
        However, the progress/status labels can still contain their original
        Turkish text when the user changes language directly from Turkish.
        This version handles both Turkish source strings and English strings.
        """

        if not isinstance(text, str) or not text:
            return text

        if self.language == "tr":
            return text

        language_translations = TRANSLATIONS.get(
            self.language,
            EN
        )

        replacements = {}

        for turkish, english in EN.items():

            localized = language_translations.get(
                turkish,
                english
            )

            replacements[turkish] = localized
            replacements[english] = localized

        for original in sorted(
            replacements.keys(),
            key=len,
            reverse=True
        ):

            text = text.replace(
                original,
                replacements[original]
            )

        return text

    def set_language(self, language):

        if self.is_converting:
            return

        if language not in LANGUAGES:
            return

        if language == self.language:

            self.close_active_menu()
            return

        selected_items = set(
            self.tree.selection()
        )

        focused_item = self.tree.focus()

        try:
            tree_position = self.tree.yview()
        except tk.TclError:
            tree_position = (0, 1)

        progress_value = self.progress["value"]
        progress_maximum = self.progress["maximum"]

        progress_text = self.progress_label.cget("text")
        status_text = self.status_bar.cget("text")

        self.close_active_menu()

        self.language = language
        self.save_language()

        # Update application window title.
        self.root.title(self.get_app_name())

        for widget in self.root.winfo_children():

            try:
                widget.destroy()
            except tk.TclError:
                pass

        self.create_menu()
        self.create_interface()

        for path in self.files:

            status = self.file_status.get(
                str(path),
                "Bekleniyor"
            )

            self.tree.insert(
                "",
                "end",
                iid=str(path),
                values=(
                    path.name,
                    str(path.parent),
                    self.tr(status)
                )
            )

            if str(path) in selected_items:
                self.tree.selection_add(str(path))

        if (
            focused_item
            and self.tree.exists(focused_item)
        ):

            self.tree.focus(focused_item)

        try:
            self.tree.yview_moveto(
                tree_position[0]
            )
        except (tk.TclError, IndexError):
            pass

        self.update_count()

        if self.output_dir:

            self.output_label.config(
                text=str(self.output_dir)
            )

        self.progress.configure(
            maximum=progress_maximum
        )

        self.progress["value"] = progress_value

        self.progress_label.config(
            text=self.translate_runtime_text(progress_text)
        )

        self.status_bar.config(
            text=self.translate_runtime_text(status_text)
        )

        self.root.update_idletasks()

        apply_titlebar_theme(self.root)

    # ========================================================
    # MENU HANDLING
    # ========================================================

    @staticmethod
    def _is_widget_inside(widget, parent):

        current = widget

        while current is not None:

            if current == parent:
                return True

            current = getattr(
                current,
                "master",
                None
            )

        return False

    def _dismiss_menu_on_outside_click(self, event):

        popup = self.active_menu

        if popup is None:
            return

        try:

            if not popup.winfo_exists():

                self.active_menu = None
                self.active_menu_button = None

                return

        except tk.TclError:

            self.active_menu = None
            self.active_menu_button = None

            return

        if self._is_widget_inside(
            event.widget,
            popup
        ):
            return

        for trigger in self.menu_trigger_widgets:

            if self._is_widget_inside(
                event.widget,
                trigger
            ):
                return

        self.close_active_menu()

    def close_active_menu(self):

        popup = self.active_menu

        self.active_menu = None
        self.active_menu_button = None

        if popup is not None:

            try:

                if popup.winfo_exists():
                    popup.destroy()

            except tk.TclError:
                pass

    # ========================================================
    # STYLE
    # ========================================================

    def setup_style(self):

        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "Midnight.Horizontal.TProgressbar",
            troughcolor=CARD,
            background=ACCENT_HOVER,
            bordercolor=CARD,
            lightcolor=ACCENT_HOVER,
            darkcolor=ACCENT_HOVER,
            thickness=12
        )

        style.configure(
            "Treeview",
            background=CARD,
            foreground=TEXT,
            fieldbackground=CARD,
            borderwidth=0,
            rowheight=36,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background=PANEL,
            foreground=MUTED,
            relief="flat",
            font=("Segoe UI", 9, "bold"),
            padding=10
        )

        style.map(
            "Treeview",
            background=[
                ("selected", "#304C78")
            ],
            foreground=[
                ("selected", "#FFFFFF")
            ]
        )

        style.map(
            "Treeview.Heading",
            background=[
                ("active", CARD_HOVER)
            ]
        )

    # ========================================================
    # LANGUAGE PNG LOADER
    # ========================================================

    def load_language_icon(self):

        try:

            if not LANGUAGE_ICON_PATH.is_file():
                return None

            image = tk.PhotoImage(
                file=str(LANGUAGE_ICON_PATH)
            )

            width = image.width()
            height = image.height()

            factor = max(
                1,
                math.ceil(max(width, height) / 24)
            )

            if factor > 1:
                image = image.subsample(
                    factor,
                    factor
                )

            return image

        except (tk.TclError, OSError) as error:

            print(
                f"Language icon loading error: {error}"
            )

            return None

    # ========================================================
    # MENU BAR
    # ========================================================

    def create_menu(self):

        self.root.config(menu="")

        self.menu_bar = tk.Frame(
            self.root,
            bg=PANEL,
            height=44
        )

        self.menu_bar.pack(
            side="top",
            fill="x"
        )

        self.menu_bar.pack_propagate(False)

        menu_font = ("Segoe UI", 9)

        self.menu_buttons = []
        self.menu_trigger_widgets = []

        # ----------------------------------------------------
        # POPUP MENU
        # ----------------------------------------------------

        def open_menu(menu_data, button):

            if self.is_converting:
                return

            if (
                self.active_menu is not None
                and self.active_menu_button == button
            ):

                self.close_active_menu()
                return

            self.close_active_menu()

            popup = tk.Toplevel(self.root)

            popup.overrideredirect(True)
            popup.configure(bg=BORDER)

            self.active_menu = popup
            self.active_menu_button = button

            x = button.winfo_rootx()

            y = (
                button.winfo_rooty()
                + button.winfo_height()
            )

            popup.geometry(
                f"+{x}+{y}"
            )

            border_frame = tk.Frame(
                popup,
                bg=BORDER,
                padx=1,
                pady=1
            )

            border_frame.pack(
                fill="both",
                expand=True
            )

            menu_frame = tk.Frame(
                border_frame,
                bg=PANEL
            )

            menu_frame.pack(
                fill="both",
                expand=True
            )

            for item in menu_data:

                if item is None:

                    tk.Frame(
                        menu_frame,
                        bg=BORDER,
                        height=1
                    ).pack(
                        fill="x",
                        padx=8,
                        pady=5
                    )

                    continue

                label, command, accelerator = item

                item_frame = tk.Frame(
                    menu_frame,
                    bg=PANEL,
                    cursor="hand2"
                )

                item_frame.pack(
                    fill="x",
                    padx=3,
                    pady=1
                )

                item_label = tk.Label(
                    item_frame,
                    text=label,
                    bg=PANEL,
                    fg=TEXT,
                    font=menu_font,
                    anchor="w",
                    padx=12,
                    pady=7,
                    cursor="hand2"
                )

                item_label.pack(
                    side="left",
                    fill="x",
                    expand=True
                )

                if accelerator:

                    tk.Label(
                        item_frame,
                        text=accelerator,
                        bg=PANEL,
                        fg=MUTED,
                        font=("Segoe UI", 8),
                        padx=12,
                        cursor="hand2"
                    ).pack(
                        side="right"
                    )

                def on_enter(
                    event,
                    frame=item_frame
                ):

                    frame.configure(
                        bg=CARD_HOVER
                    )

                    for child in frame.winfo_children():
                        child.configure(bg=CARD_HOVER)

                def on_leave(
                    event,
                    frame=item_frame
                ):

                    frame.configure(
                        bg=PANEL
                    )

                    for child in frame.winfo_children():
                        child.configure(bg=PANEL)

                def on_click(
                    event,
                    action=command
                ):

                    self.close_active_menu()

                    if action:

                        self.root.after(
                            10,
                            action
                        )

                for widget in item_frame.winfo_children():

                    widget.bind(
                        "<Enter>",
                        on_enter
                    )

                    widget.bind(
                        "<Leave>",
                        on_leave
                    )

                    widget.bind(
                        "<Button-1>",
                        on_click
                    )

                item_frame.bind(
                    "<Enter>",
                    on_enter
                )

                item_frame.bind(
                    "<Leave>",
                    on_leave
                )

                item_frame.bind(
                    "<Button-1>",
                    on_click
                )

            popup.bind(
                "<Escape>",
                lambda event: self.close_active_menu()
            )

            popup.focus_force()

        # ----------------------------------------------------
        # DROPDOWN BUTTON
        # ----------------------------------------------------

        def create_dropdown(title, commands):

            button = tk.Button(
                self.menu_bar,
                text=title,
                bg=PANEL,
                fg=TEXT,
                activebackground=CARD_HOVER,
                activeforeground="#FFFFFF",
                font=menu_font,
                padx=15,
                pady=0,
                relief="flat",
                bd=0,
                highlightthickness=0,
                cursor="hand2",
                takefocus=True
            )

            button.pack(
                side="left",
                fill="y"
            )

            button.configure(
                command=lambda data=commands, b=button:
                open_menu(data, b)
            )

            button.bind(
                "<Enter>",
                lambda event, b=button:
                b.configure(bg=CARD_HOVER)
            )

            button.bind(
                "<Leave>",
                lambda event, b=button:
                b.configure(bg=PANEL)
            )

            self.menu_buttons.append(button)
            self.menu_trigger_widgets.append(button)

        # FILE MENU

        create_dropdown(
            self.tr("Dosya"),
            [
                (
                    self.tr("DDS Dosyası Ekle"),
                    self.add_files,
                    "Ctrl+O"
                ),
                (
                    self.tr("Çıktı Klasörü Seç"),
                    self.select_output,
                    ""
                ),
                None,
                (
                    self.tr("Listeyi Temizle"),
                    self.clear_files,
                    "Ctrl+L"
                ),
                None,
                (
                    self.tr("Çıkış"),
                    self.on_close,
                    ""
                )
            ]
        )

        # TOOLS MENU

        create_dropdown(
            self.tr("Araçlar"),
            [
                (
                    self.tr("Seçilenleri Kaldır"),
                    self.remove_selected,
                    "Delete"
                ),
                (
                    self.tr("Seçilenleri Dönüştür"),
                    self.convert_selected,
                    ""
                ),
                (
                    self.tr("Tümünü Dönüştür"),
                    self.convert_all,
                    ""
                )
            ]
        )

        # HELP MENU

        create_dropdown(
            self.tr("Yardım"),
            [
                (
                    self.tr("Hakkında"),
                    self.about,
                    ""
                )
            ]
        )

        # ----------------------------------------------------
        # LANGUAGE SELECTOR
        # ----------------------------------------------------

        language_frame = tk.Frame(
            self.menu_bar,
            bg=PANEL,
            cursor="hand2"
        )

        language_frame.pack(
            side="right",
            fill="y",
            padx=(0, 12)
        )

        self.language_icon = self.load_language_icon()

        language_button = tk.Button(
            language_frame,
            text=self.tr("Dil"),
            image=self.language_icon,
            compound="left",
            bg=PANEL,
            fg=TEXT,
            activebackground=CARD_HOVER,
            activeforeground="#FFFFFF",
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=0,
            relief="flat",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            takefocus=True
        )

        language_button.pack(
            side="left",
            fill="y"
        )

        def get_language_commands():

            return [
                (
                    (
                        "✓  "
                        if code == self.language
                        else "     "
                    ) + name,

                    lambda lang=code: self.set_language(lang),
                    ""
                )
                for code, name in LANGUAGES.items()
            ]

        language_button.configure(
            command=lambda:
            open_menu(
                get_language_commands(),
                language_frame
            )
        )

        self.menu_trigger_widgets.extend(
            [
                language_frame,
                language_button
            ]
        )

        # ----------------------------------------------------
        # LANGUAGE HOVER EFFECT
        # ----------------------------------------------------

        def language_hover_enter(event=None):

            language_frame.configure(bg=CARD_HOVER)
            language_button.configure(bg=CARD_HOVER)

        def language_hover_leave(event=None):

            language_frame.configure(bg=PANEL)
            language_button.configure(bg=PANEL)

        for widget in (
            language_frame,
            language_button
        ):

            widget.bind(
                "<Enter>",
                language_hover_enter
            )

            widget.bind(
                "<Leave>",
                language_hover_leave
            )

    # ========================================================
    # MAIN INTERFACE
    # ========================================================

    def create_interface(self):

        # HEADER

        header = tk.Frame(
            self.root,
            bg=PANEL,
            padx=28,
            pady=20
        )

        header.pack(fill="x")

        header_top = tk.Frame(
            header,
            bg=PANEL
        )

        header_top.pack(fill="x")

        tk.Label(
            header_top,
            text=self.get_app_name(),
            bg=PANEL,
            fg=TEXT,
            font=("Segoe UI", 21, "bold")
        ).pack(side="left")

        tk.Label(
            header_top,
            text="DDS  ⟶  PNG",
            bg="#263B60",
            fg="#A8C8FF",
            padx=12,
            pady=5,
            font=("Segoe UI", 9, "bold")
        ).pack(side="right")

        tk.Label(
            header,
            text=(
                f"{self.tr('Doku Dönüştürme Stüdyosu')}  |  "
                f"{DEVELOPER}"
            ),
            bg=PANEL,
            fg=MUTED,
            font=("Segoe UI", 10)
        ).pack(
            anchor="w",
            pady=(7, 0)
        )

        # STATUS BAR

        self.status_bar = tk.Label(
            self.root,
            text="  " + self.tr("Hazır"),
            bg="#090D17",
            fg=MUTED,
            anchor="w",
            padx=20,
            pady=8,
            font=("Segoe UI", 8)
        )

        self.status_bar.pack(
            side="bottom",
            fill="x"
        )

        # BOTTOM PANEL

        bottom = tk.Frame(
            self.root,
            bg=PANEL,
            padx=28,
            pady=17
        )

        bottom.pack(
            side="bottom",
            fill="x"
        )

        # CONVERSION BUTTONS

        convert_frame = tk.Frame(
            bottom,
            bg=PANEL
        )

        convert_frame.pack(
            fill="x",
            pady=(0, 17)
        )

        self.convert_selected_button = RoundedButton(
            convert_frame,
            self.tr("Seçilenleri Dönüştür"),
            self.convert_selected,
            ACCENT,
            ACCENT_HOVER
        )

        self.convert_selected_button.pack(
            side="left",
            padx=(0, 10)
        )

        self.convert_all_button = RoundedButton(
            convert_frame,
            self.tr("Tümünü Dönüştür"),
            self.convert_all,
            PURPLE,
            PURPLE_HOVER
        )

        self.convert_all_button.pack(
            side="left"
        )

        # PROGRESS HEADER

        progress_header = tk.Frame(
            bottom,
            bg=PANEL
        )

        progress_header.pack(
            fill="x",
            pady=(0, 8)
        )

        tk.Label(
            progress_header,
            text=self.tr("DÖNÜŞTÜRME İLERLEMESİ"),
            bg=PANEL,
            fg=TEXT,
            font=("Segoe UI", 9, "bold")
        ).pack(side="left")

        self.progress_label = tk.Label(
            progress_header,
            text=self.tr("Bekleniyor..."),
            bg=PANEL,
            fg=MUTED,
            font=("Segoe UI", 9)
        )

        self.progress_label.pack(side="right")

        self.progress = ttk.Progressbar(
            bottom,
            maximum=100,
            mode="determinate",
            style="Midnight.Horizontal.TProgressbar"
        )

        self.progress.pack(
            fill="x",
            pady=(0, 17)
        )

        # FOOTER

        footer = tk.Frame(
            bottom,
            bg=PANEL
        )

        footer.pack(fill="x")

        tk.Label(
            footer,
            text=(
                f"{self.tr('SÜRÜM')} {VERSION}  |  "
                "MIDNIGHT PRO"
            ),
            bg=PANEL,
            fg=MUTED,
            font=("Segoe UI", 8)
        ).pack(side="right")

        # MAIN AREA

        main = tk.Frame(
            self.root,
            bg=BG,
            padx=28,
            pady=20
        )

        main.pack(
            fill="both",
            expand=True
        )

        # FILE LIST HEADER

        top = tk.Frame(
            main,
            bg=BG
        )

        top.pack(
            fill="x",
            pady=(0, 12)
        )

        tk.Label(
            top,
            text=self.tr("DOSYA LİSTESİ"),
            bg=BG,
            fg=TEXT,
            font=("Segoe UI", 11, "bold")
        ).pack(side="left")

        self.file_count = tk.Label(
            top,
            text=f"0 {self.tr('dosya')}",
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 9)
        )

        self.file_count.pack(side="right")

        # FILE TABLE

        table_frame = tk.Frame(
            main,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        table_frame.pack(
            fill="both",
            expand=True
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=(
                "filename",
                "location",
                "status"
            ),
            show="headings",
            selectmode="extended"
        )

        self.tree.heading(
            "filename",
            text=self.tr("Dosya Adı")
        )

        self.tree.heading(
            "location",
            text=self.tr("Dosya Konumu")
        )

        self.tree.heading(
            "status",
            text=self.tr("Durum")
        )

        self.tree.column(
            "filename",
            width=210,
            minwidth=140
        )

        self.tree.column(
            "location",
            width=390,
            minwidth=150
        )

        self.tree.column(
            "status",
            width=120,
            minwidth=100,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # FILE BUTTONS

        buttons = tk.Frame(
            main,
            bg=BG
        )

        buttons.pack(
            fill="x",
            pady=15
        )

        RoundedButton(
            buttons,
            self.tr("+ Dosya Ekle"),
            self.add_files,
            ACCENT,
            ACCENT_HOVER
        ).pack(
            side="left",
            padx=(0, 8)
        )

        RoundedButton(
            buttons,
            self.tr("Seçilenleri Kaldır"),
            self.remove_selected,
            CARD,
            CARD_HOVER
        ).pack(
            side="left",
            padx=4
        )

        RoundedButton(
            buttons,
            self.tr("Listeyi Temizle"),
            self.clear_files,
            CARD,
            CARD_HOVER
        ).pack(
            side="left",
            padx=4
        )

        # OUTPUT FOLDER

        output_frame = tk.Frame(
            main,
            bg=CARD,
            padx=16,
            pady=14,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        output_frame.pack(fill="x")

        tk.Label(
            output_frame,
            text=self.tr("ÇIKTI KLASÖRÜ"),
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 9, "bold")
        ).pack(anchor="w")

        output_row = tk.Frame(
            output_frame,
            bg=CARD
        )

        output_row.pack(
            fill="x",
            pady=(9, 0)
        )

        output_text = (
            str(self.output_dir)
            if self.output_dir
            else self.tr(
                "Kaynak dosyaların bulunduğu klasör"
            )
        )

        self.output_label = tk.Label(
            output_row,
            text=output_text,
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 9),
            anchor="w"
        )

        self.output_label.pack(
            side="left",
            fill="x",
            expand=True
        )

        RoundedButton(
            output_row,
            self.tr("Klasör Seç"),
            self.select_output,
            "#263B60",
            "#34517F"
        ).pack(side="right")

    # ========================================================
    # FILE OPERATIONS
    # ========================================================

    def add_files(self):

        if self.is_converting:
            return

        selected = filedialog.askopenfilenames(
            parent=self.root,
            title=self.tr("DDS Dosyalarını Seç"),
            filetypes=[
                (
                    self.tr("DDS Dosyaları"),
                    "*.dds"
                ),
                (
                    self.tr("Tüm Dosyalar"),
                    "*.*"
                )
            ]
        )

        if not selected:
            return

        added = 0

        for filename in selected:

            path = Path(filename)

            if path.suffix.lower() != ".dds":
                continue

            if path in self.files:
                continue

            self.files.append(path)

            self.file_status[str(path)] = "Bekleniyor"

            self.tree.insert(
                "",
                "end",
                iid=str(path),
                values=(
                    path.name,
                    str(path.parent),
                    self.tr("Bekleniyor")
                )
            )

            added += 1

        self.update_count()

        status_text = (
            f"{added} {self.tr('yeni dosya eklendi.')}"
        )

        self.set_status(status_text)

    def remove_selected(self):

        if self.is_converting:
            return

        selected = self.tree.selection()

        for item in selected:

            path = Path(item)

            if path in self.files:
                self.files.remove(path)

            self.file_status.pop(
                str(path),
                None
            )

            self.tree.delete(item)

        self.update_count()

        self.set_status(
            self.tr("Seçilen dosyalar kaldırıldı.")
        )

    def clear_files(self):

        if self.is_converting:
            return

        if not self.files:
            return

        self.files.clear()
        self.file_status.clear()

        for item in self.tree.get_children():
            self.tree.delete(item)

        self.progress["value"] = 0

        self.progress_label.config(
            text=self.tr("Bekleniyor...")
        )

        self.update_count()

        self.set_status(
            self.tr("Dosya listesi temizlendi.")
        )

    def update_count(self):

        self.file_count.config(
            text=f"{len(self.files)} {self.tr('dosya')}"
        )

    # ========================================================
    # OUTPUT FOLDER
    # ========================================================

    def select_output(self):

        if self.is_converting:
            return

        folder = filedialog.askdirectory(
            parent=self.root,
            title=self.tr("Çıktı Klasörünü Seç")
        )

        if not folder:
            return

        self.output_dir = Path(folder)

        self.output_label.config(
            text=str(self.output_dir)
        )

        self.set_status(
            self.tr("Çıktı klasörü güncellendi.")
        )

    # ========================================================
    # CONVERSION
    # ========================================================

    def convert_selected(self):

        if self.is_converting:
            return

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                self.tr("Dosya Seçilmedi"),
                self.tr(
                    "Lütfen dönüştürmek istediğiniz dosyaları seçin."
                ),
                parent=self.root
            )

            return

        paths = [
            Path(item)
            for item in selected
        ]

        self.convert_files(paths)

    def convert_all(self):

        if self.is_converting:
            return

        if not self.files:

            messagebox.showwarning(
                self.tr("Dosya Bulunamadı"),
                self.tr("Önce DDS dosyası ekleyin."),
                parent=self.root
            )

            return

        self.convert_files(
            self.files.copy()
        )

    def convert_files(self, paths):

        if self.is_converting:
            return

        if not paths:
            return

        self.texconv_path = self.check_texconv()

        if not self.texconv_path:
            return

        self.is_converting = True

        self.conversion_paths = list(paths)
        self.conversion_index = 0

        self.successful = 0
        self.failed = 0
        self.skipped = 0

        self.conversion_total = len(paths)

        self.progress["value"] = 0
        self.progress["maximum"] = self.conversion_total

        self.convert_selected_button.config(
            state="disabled"
        )

        self.convert_all_button.config(
            state="disabled"
        )

        self.set_status(
            self.tr("Dönüştürülüyor:")
        )

        self.process_next_file()

    def process_next_file(self):

        if not self.is_converting:
            return

        if self.conversion_index >= self.conversion_total:

            self.finish_conversion()
            return

        input_path = self.conversion_paths[
            self.conversion_index
        ]

        self.progress_label.config(
            text=(
                f"{self.tr('Dönüştürülüyor:')} "
                f"{input_path.name}"
            )
        )

        if self.output_dir:

            output_path = (
                self.output_dir
                / input_path.with_suffix(".png").name
            )

        else:

            output_path = input_path.with_suffix(".png")

        if output_path.exists():

            overwrite = messagebox.askyesno(
                self.tr("Aynı isimli dosya var"),
                (
                    f"{self.tr('Dosya zaten mevcut:')}\n"
                    f"{output_path}\n\n"
                    f"{self.tr('Üzerine yazılsın mı?')}"
                ),
                parent=self.root
            )

            if not overwrite:

                self.skipped += 1

                self.conversion_index += 1

                self.update_conversion_progress()

                self.root.after(
                    1,
                    self.process_next_file
                )

                return

        worker = threading.Thread(
            target=self._conversion_worker,
            args=(
                self.texconv_path,
                input_path,
                output_path
            ),
            daemon=True
        )

        worker.start()

        self.root.after(
            100,
            self.check_conversion_queue
        )

    def _conversion_worker(
        self,
        texconv_path,
        input_path,
        output_path
    ):

        try:

            output_path.parent.mkdir(
                parents=True,
                exist_ok=True
            )

            command = [
                texconv_path,
                "-ft",
                "png",
                "-o",
                str(output_path.parent),
                "-y",
                str(input_path)
            ]

            creation_flags = 0

            if hasattr(subprocess, "CREATE_NO_WINDOW"):
                creation_flags = subprocess.CREATE_NO_WINDOW

            result = subprocess.run(
                command,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                creationflags=creation_flags
            )

            if result.returncode != 0:

                error_message = (
                    result.stderr.strip()
                    or result.stdout.strip()
                    or f"Texconv exited with code {result.returncode}"
                )

                raise RuntimeError(error_message)

            if not output_path.is_file():

                raise RuntimeError(
                    "Texconv completed but the PNG output file was not found."
                )

            self.conversion_queue.put(
                (
                    "success",
                    input_path,
                    None
                )
            )

        except Exception as error:

            self.conversion_queue.put(
                (
                    "error",
                    input_path,
                    str(error)
                )
            )

    def check_conversion_queue(self):

        if not self.is_converting:
            return

        try:

            result = self.conversion_queue.get_nowait()

        except queue.Empty:

            self.root.after(
                100,
                self.check_conversion_queue
            )

            return

        status, input_path, error = result

        if status == "success":

            self.successful += 1

            self.file_status[str(input_path)] = "Tamamlandı"

            self.tree.set(
                str(input_path),
                "status",
                self.tr("Tamamlandı")
            )

        else:

            self.failed += 1

            self.file_status[str(input_path)] = "Hata"

            self.tree.set(
                str(input_path),
                "status",
                self.tr("Hata")
            )

            print(
                f"{input_path.name}: {error}"
            )

        self.conversion_index += 1

        self.update_conversion_progress()

        self.root.after(
            1,
            self.process_next_file
        )

    def update_conversion_progress(self):

        self.progress["value"] = self.conversion_index

        self.progress_label.config(
            text=(
                f"{self.tr('İşlem ilerlemesi:')} "
                f"{self.conversion_index}/"
                f"{self.conversion_total}"
            )
        )

    def finish_conversion(self):

        self.is_converting = False

        self.convert_selected_button.config(
            state="normal"
        )

        self.convert_all_button.config(
            state="normal"
        )

        self.progress["value"] = self.conversion_total

        self.progress_label.config(
            text=(
                f"{self.tr('Tamamlandı:')} "
                f"{self.successful} | "
                f"{self.tr('Hatalı:')} "
                f"{self.failed}"
            )
        )

        self.set_status(
            f"{self.tr('Dönüştürme tamamlandı. Başarılı:')} "
            f"{self.successful}, "
            f"{self.tr('Hatalı:')} "
            f"{self.failed}"
        )

        messagebox.showinfo(
            self.tr("İşlem Tamamlandı"),
            (
                f"{self.tr('Dönüştürme işlemi tamamlandı.')}\n\n"
                f"{self.tr('Başarılı:')} {self.successful}\n"
                f"{self.tr('Hatalı:')} {self.failed}"
            ),
            parent=self.root
        )

    # ========================================================
    # ABOUT
    # ========================================================

    def about(self):

        messagebox.showinfo(
            self.tr("Hakkında"),
            (
                f"{self.get_app_name()}\n\n"
                f"{self.tr('Sürüm:')} {VERSION}\n"
                f"{self.tr('Geliştirici:')} {DEVELOPER}\n\n"
                f"{self.tr('DDS dosyalarını PNG formatına dönüştürür.')}\n\n"
                f"{self.tr('Python ve DirectXTex tarafından desteklenmektedir.')}"
            ),
            parent=self.root
        )

    # ========================================================
    # STATUS
    # ========================================================

    def set_status(self, text):

        self.status_bar.config(
            text=f"  {text}"
        )

    # ========================================================
    # EXIT
    # ========================================================

    def on_close(self):

        if self.is_converting:

            messagebox.showwarning(
                self.tr("Hata"),
                self.tr(
                    "Dönüştürme sırasında çıkış yapılamaz."
                ),
                parent=self.root
            )

            return

        self.close_active_menu()

        self.root.destroy()


# ============================================================
# PROGRAM ENTRY
# ============================================================

def main():

    root = tk.Tk()

    try:

        app = DDSConverter(root)

    except Exception as error:

        root.destroy()

        messagebox.showerror(
            "Application Error",
            str(error)
        )

        return

    root.mainloop()


if __name__ == "__main__":
    main()
