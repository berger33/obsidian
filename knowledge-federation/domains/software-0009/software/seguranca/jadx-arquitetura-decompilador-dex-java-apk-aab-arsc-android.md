---
id: software.seguranca.tranche10.000921
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
fontes: ["https://raw.githubusercontent.com/skylot/jadx/master/README.md", "https://github.com/skylot/jadx/wiki/jadx-gui-features-overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **JADX (`skylot/jadx`)**: Arquitetura do Decompilador **Dalvik/ART Bytecode (`.dex`) para Java** e Decodificador Nativo de `.apk`, `.aab` e `resources.arsc`

## Em uma frase
**JADX** (`skylot/jadx`, licença Apache 2.0, mantido por `@skylot`, disponível em CLI `jadx` e interface gráfica `jadx-gui`) é a ferramenta open-source padrão da indústria para **Engenharia Reversa e Auditoria de Segurança de Aplicações Android (OWASP MASVS / MASTG)**.

## Por que importa
Diferente de fluxos antigos que exigiam encadear três ferramentas separadas (`dex2jar` para converter `.dex` em `.jar` + `jd-gui` para ver o Java + `apktool` para ler o XML), o JADX lê diretamente **`.apk`, `.aab` (*Android App Bundle*), `.dex`, `.aar`, `.jar`, `.class`, `.smali`, `.arsc`, `.xapk` e `.apkm`**, reconstruindo simultaneamente a árvore de **código-fonte Java/Kotlin** e decodificando os arquivos binários **`AndroidManifest.xml`** e **`resources.arsc`**!

## Como funciona
Na linha de comando (`jadx`), você pode decompilar um APK inteiro em paralelo usando múltiplas threads (`-j 16`, padrão) e separar o código-fonte (`-ds`) dos recursos decodificados (`-dr`) para alimentar ferramentas de SAST, `semgrep`, `gitleaks` ou `yara`!

## Exemplo
```bash
# Decompilar um aplicativo Android (.apk) em linha de comando com 16 threads (-j 16) salvando Java e Recursos em pastas dedicadas
jadx --version
jadx -d /cases/mobile/app_decompiled \
  -ds /cases/mobile/app_decompiled/sources \
  -dr /cases/mobile/app_decompiled/resources \
  -j 16 \
  /cases/mobile/target_app.apk
```

## Limites e trade-offs
Atenção a um recurso de segurança importantíssimo do próprio JADX ao analisar APKs maliciosos (Malware Android que usa **Zip Bomb**, **Path Traversal `../../` no ZIP** ou **XML Bomb / XXE no `AndroidManifest.xml`**): o JADX possui proteções nativas de segurança de ZIP e XML ativas por padrão! Jamais defina `JADX_DISABLE_ZIP_SECURITY=true` ou `JADX_DISABLE_XML_SECURITY=true` ao analisar APKs de fontes não confiáveis fora de uma sandbox isolada (**Bubblewrap**)!

## Como verificar
Verifique após a execução a estrutura gerada em `/cases/mobile/app_decompiled/resources/AndroidManifest.xml` e `/cases/mobile/app_decompiled/sources/`.

## Conexões
- [[jadx-modos-decompilacao-restructure-simple-fallback-show-bad-code]] — Veja também: JADX: Modos de Decompilação (**`-m auto | restructure | simple | fallback`**) e **`--show-bad-code`** para Métodos Ofuscados que Falham no AST.
- [[jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin]] — Referência cruzada direta com jadx-desofuscacao-automatica-deobf-mappings-proguard-r8-kotlin.
- [[apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali]] — Referência cruzada direta com apktool-arquitetura-decodificacao-resources-arsc-axml-baksmali.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
