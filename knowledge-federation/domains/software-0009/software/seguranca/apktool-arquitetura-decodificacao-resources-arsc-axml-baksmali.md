---
id: software.seguranca.tranche10.000931
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

# **Apktool (`iBotPeaches/Apktool`)**: Arquitetura de Decodificação de **Binary XML (`AXML`), `resources.arsc`** e Disassembly **Smali (`baksmali`/`smali`)**

## Em uma frase
Se você simplesmente descompactar um arquivo `.apk` com `unzip app.apk`, descobrirá que o `AndroidManifest.xml` e os layouts em `res/` **não são XML em texto legível**, mas sim **Android Binary XML (`AXML`)** compilado pelo `aapt2`, a tabela de recursos está compactada em **`resources.arsc`**, e o código está em bytecode binário **`classes.dex`**!

## Por que importa
**Apktool** (`iBotPeaches/Apktool`, licença Apache 2.0, mantido por Connor Tumbleson / `@iBotPeaches`) é a ferramenta oficial para o **ciclo completo de Desmontagem (`apktool d`) -> Modificação (Smali / XML / Assets) -> Recompilação Funcional (`apktool b`)** de pacotes Android!

## Como funciona
Ao rodar **`apktool d app.apk`**, o Apktool realiza três tarefas coordenadas: **(1)** decodifica a tabela `resources.arsc` e reconstrói todos os XMLs (`AndroidManifest.xml`, `res/values/strings.xml`, `res/xml/network_security_config.xml`) e imagens 9-patch (`.9.png`) de volta ao formato de código-fonte editável; **(2)** desmonta cada arquivo `classes.dex`, `classes2.dex`, ... em código assembly Dalvik legível (**`.smali`**) usando o **`baksmali`** embutido; e **(3)** grava os metadados de versão/SDK no manifesto de projeto **`apktool.yml`**!

## Exemplo
```bash
# Verificar a versao do Apktool e decodificar completamente (recursos + smali) um aplicativo Android para auditoria e patching
apktool --version
apktool d /cases/mobile/target_app.apk -o /cases/mobile/apktool_decoded
```

## Limites e trade-offs
Compreenda a divisão de papéis complementar entre **JADX** e **Apktool**: você usa o **JADX** para **ler e auditar rapidamente o código em Java/Kotlin de alto nível**, e usa o **Apktool** quando precisa **editar o `AndroidManifest.xml`, alterar `network_security_config.xml`, injetar o `frida-gadget.so` ou modificar instruções `.smali` e recompilar um novo `.apk` funcional**!

## Como verificar
Inspecione o arquivo `/cases/mobile/apktool_decoded/apktool.yml` gerado para ver o `minSdkVersion`, `targetSdkVersion` e a lista de `doNotCompress`.

## Conexões
- [[apktool-controles-decodificacao-no-src-no-res-only-main-classes]] — Veja também: Apktool (`d` / `decode`): Uso Cirúrgico de **`-s` (`--no-src`)**, **`-r` (`--no-res`)** e **`--only-main-classes`** para Evitar Erros de `aapt2` em APKs Complexos.
- [[apktool-modificacao-androidmanifest-debuggable-network-security-config]] — Referência cruzada direta com apktool-modificacao-androidmanifest-debuggable-network-security-config.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
