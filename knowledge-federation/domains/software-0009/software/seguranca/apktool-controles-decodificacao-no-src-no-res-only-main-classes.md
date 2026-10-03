---
id: software.seguranca.tranche10.000932
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

# Apktool (`d` / `decode`): Uso Cirúrgico de **`-s` (`--no-src`)**, **`-r` (`--no-res`)** e **`--only-main-classes`** para Evitar Erros de `aapt2` em APKs Complexos

## Em uma frase
Em aplicativos bancários ou corporativos modernos que usam recursos proprietários ou ofuscação da tabela `resources.arsc` (AndResGuard), tentar decodificar e recompilar simultaneamente todos os recursos e todos os arquivos DEX pode causar erros de compilação no `aapt2` ou demorar vários minutos.

## Por que importa
O Apktool oferece três flags essenciais no subcomando `d` (`decode`) para isolar apenas o que você realmente precisa modificar: **(1) `-s` / `--no-src`** (decodifica apenas o `AndroidManifest.xml` e `res/`, mantendo os arquivos `classes*.dex` binários intactos sem desmontar para Smali!); **(2) `-r` / `--no-res`** (desmonta apenas `classes*.dex` para `.smali`, mantendo `resources.arsc` e os XMLs binários intactos sem tocar nos recursos!); e **(3) `--only-main-classes`** (desmonta apenas os arquivos `classes[0-9]*.dex` na raiz, ignorando DEX secundários escondidos em `assets/`)!

## Como funciona
Escolher a flag certa elimina 90% das falhas de recompilação (`apktool b`) em APKs reais!

## Exemplo
```bash
# Caso 1: Voce quer apenas editar o AndroidManifest.xml ou network_security_config.xml sem mexer no codigo DEX (-s / --no-src)
apktool d -s /cases/mobile/target_app.apk -o /cases/mobile/apk_edit_xml_only

# Caso 2: Voce quer apenas alterar a logica de um metodo em Smali sem tocar nos recursos complexos (-r / --no-res)
apktool d -r /cases/mobile/target_app.apk -o /cases/mobile/apk_edit_smali_only
```

## Limites e trade-offs
Grave esta regra prática de ouro: se o seu objetivo é **apenas adicionar `network_security_config.xml` ou `android:debuggable="true"`**, use SEMPRE **`apktool d -s`** (não toque no DEX!); se o seu objetivo é **apenas fazer patch em um `if-eqz` no código Smali**, use SEMPRE **`apktool d -r`** (não toque nos recursos XML/ARSC!)!

## Como verificar
Compare o tempo de execução de `apktool d -s` (geralmente menos de 3 segundos!) contra a decodificação completa.

## Conexões
- [[apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali]] — Veja também: **Apktool (`iBotPeaches/Apktool`)**: Arquitetura de Decodificação de **Binary XML (`AXML`), `resources.arsc`** e Disassembly **Smali (`baksmali`/`smali`)**.
- [[apktool-modificacao-androidmanifest-debuggable-network-security-config]] — Veja também: Apktool na Prática: Habilitando **Interceptação HTTPS de CAs de Usuário (`network_security_config.xml`)** e **`android:debuggable="true"`** em Android 7+.
- [[apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3]] — Referência cruzada direta com apktool-recompilacao-build-use-aapt2-zipalign-apksigner-v2-v3.
- [[jadx-auditoria-androidmanifest-exported-components-deep-links-permissions]] — Referência cruzada direta com jadx-auditoria-androidmanifest-exported-components-deep-links-permissions.

## Fontes
- [Apktool Official GitHub Repository — Reverse Engineering Android APK Resources & Smali](https://raw.githubusercontent.com/iBotPeaches/Apktool/main/README.md) — repositório oficial do Apktool cobrindo decodificação de recursos binários Android e reconstrução de pacotes APK; consultado em 2026-10-03.
- [Apktool Official Documentation — Introduction to APK Structure, AXML Decoding & Baksmali](https://apktool.org/wiki/the-basics/intro/) — documentação oficial do Apktool detalhando a decodificação de `AndroidManifest.xml`, `resources.arsc` e desmontagem `classes.dex`; consultado em 2026-10-03.
