---
id: software.seguranca.tranche10.000927
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

# JADX: Exportação de **Control Flow Graphs (`--cfg`, `--raw-cfg`)**, **Grafo de Chamadas (`--call-graph json|dot`)** e Saída Estruturada (`--output-format json`)

## Em uma frase
Para análises estáticas automatizadas e rastreamento de fluxo de dados (*Taint Tracking* entre uma fonte não-confiável como `getIntent().getStringExtra()` e um sumidouro perigoso como `rawQuery()` ou `Runtime.getRuntime().exec()`), o JADX permite exportar a representação interna do programa em formatos de grafo e JSON!

## Por que importa
Conforme documentado no `README.md` oficial, a flag **`--call-graph json`** (ou `--call-graph dot` para visualización no Graphviz) salva o **Grafo Completo de Chamadas de Métodos (*Call Graph*)** de todo o aplicativo; enquanto **`--cfg`** e **`--raw-cfg`** exportam os **Grafos de Fluxo de Controle (*Control Flow Graphs*)** de cada método em arquivos `.dot`!

## Como funciona
Além disso, passar **`--output-format json`** faz o JADX exportar a estrutura de classes, métodos, campos e instruções decompiladas em **JSON estruturado** em vez de arquivos `.java`!

## Exemplo
```bash
# Exportar o Grafo de Chamadas completo do aplicativo Android em formato JSON (--call-graph json) para analise de alcançabilidade
jadx -d /cases/mobile/app_graphs \
  --call-graph json \
  --no-res \
  /cases/mobile/target_app.apk
```

## Limites e trade-offs
Por que o **`--call-graph json`** é tão útil ao auditar vulnerabilidades em bibliotecas de terceiros (SCA Mobile) dentro de um APK? Porque mesmo que o **OSV-Scanner** aponte que o APK embute uma biblioteca vulnerável, consultar o Call Graph do JADX responde imediatamente se algum método do seu aplicativo realmente chama a função vulnerável daquela biblioteca (*Reachability Analysis*)!

## Como verificar
Visualize arquivos `.dot` gerados por `--cfg` para métodos específicos usando `dot -Tsvg metodo.dot -o metodo.svg`.

## Conexões
- [[jadx-auditoria-webview-javascriptinterface-ssl-pinning-criptografia]] — Veja também: Auditoria de Código no JADX (**OWASP MASVS-CODE & CRYPTO**): **WebViews Inseguras (`addJavascriptInterface`)**, **`X509TrustManager` Vazio** e Criptografia Fraca.
- [[jadx-exportacao-projeto-gradle-export-gradle-android-studio-ide]] — Veja também: JADX **`-e` / `--export-gradle`**: Exportação Direta do APK/AAR como um **Projeto Gradle (`build.gradle`)** para Análise no **Android Studio / IntelliJ IDEA**.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
