---
id: software.seguranca.tranche10.000935
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md", "https://apktool.org/wiki/the-basics/intro/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Apktool + **`frida-gadget.so`**: Como Embutir o Frida Dentro de um APK via `System.loadLibrary` em Smali para Instrumentação em **Aparelhos Sem Root**

## Em uma frase
Como usar todo o poder de instrumentação dinâmica em tempo real do **Frida** quando você precisa testar um aplicativo em um **celular corporativo físico bloqueado onde não há acesso Root** (e, portanto, você não pode rodar o binário `frida-server` em `/data/local/tmp/`)?

## Por que importa
A solução clássica da engenharia de segurança mobile é empacotar a biblioteca compartilhada **`libfrida-gadget.so`** (baixada das releases oficiais do Frida para a arquitetura do celular, ex.: `arm64-v8a`) diretamente dentro do APK usando o **Apktool**!

## Como funciona
O procedimento tem 3 passos exatos: **(1)** copie o `frida-gadget-*-android-arm64.so` para **`apktool_decoded/lib/arm64-v8a/libfrida-gadget.so`**; **(2)** verifique que o `AndroidManifest.xml` possui a permissão `<uses-permission android:name="android.permission.INTERNET" />` e `android:extractNativeLibs="true"`; e **(3)** no construtor estático `<clinit>` ou no método `onCreate()` da `Application` ou `MainActivity` principal em `.smali`, adicione as duas linhas que carregam a biblioteca: **`const-string v0, "frida-gadget"`** e **`invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V`**!

## Exemplo
```smali
# Trecho inserido no inicio do metodo onCreate() ou <clinit> da MainActivity.smali para carregar o libfrida-gadget.so
const-string v0, "frida-gadget"
invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V
```

## Limites e trade-offs
Atenção ao detalhe de registradores: se o método `<clinit>` ou `onCreate` onde você inseriu `const-string v0, ...` tinha originalmente `.locals 0`, **incremente para `.locals 1`** para que o verificador de bytecode do ART (`dex2oat`) não rejeite o uso do registrador `v0`!

## Como verificar
Após recompilar, alinhar e assinar o APK modificado, basta abrir o app no celular e conectar com `frida -U Gadget`!

## Conexões
- [[apktool-engenharia-reversa-edicao-bytecode-smali-registradores-patch]] — Veja também: Apktool & **Bytecode Smali**: Anatomia de Métodos (`.locals`, `v0`/`p0`), Desvios Condicionais (`if-eqz`/`if-nez`) e Patching de *Root Detection* / *SSL Pinning*.
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Veja também: Apktool (`b` / `build`) + **`zipalign`** + **`apksigner` (v1/v2/v3/v4)**: O Pipeline Completo de Recompilação e Assinatura para Android 11–15+.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
