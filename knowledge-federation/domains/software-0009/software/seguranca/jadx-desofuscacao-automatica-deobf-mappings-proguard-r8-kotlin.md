---
id: software.seguranca.tranche10.000923
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

# JADX: Desofuscação Automática (**`--deobf`**, `.jobf`), Importação de Mapas **ProGuard/R8 (`--mappings-path`)** e Metadados **Kotlin (`kotlin.Metadata`)**

## Em uma frase
Aplicativos Android compilados em modo Release com **R8 / ProGuard** renomeiam pacotes, classes, métodos e campos para identificadores curtos ilegíveis (`a.a.a`, `b.a()`, `c.b`) — ou pior, ofuscadores maliciosos renomeiam classes para palavras reservadas do Java (`do.if.while`), caracteres Unicode invisíveis ou nomes que diferem apenas por maiúsculas/minúsculas (`A.class` vs `a.class`, que colidem e sobrescrevem um ao outro ao extrair em sistemas de arquivos case-insensitive do Windows/macOS!).

## Por que importa
O JADX resolve todos esses problemas através de três motores documentados no `README.md`: **(1) `--deobf`** (renomeia automaticamente qualquer identificador menor que `--deobf-min 3` ou maior que `--deobf-max 64` para aliases únicos legíveis como `C0142a`, `m284b` e salva o mapa no arquivo **`.jobf`**!) combinado com **`--rename-flags case,valid,printable`**; **(2) `--mappings-path <mapping.txt>`** (carrega arquivos de mapeamento `PROGUARD_FILE`, `TINY_FILE`, `ENIGMA_FILE`, `JOBF_FILE`); e **(3) Plugin `kotlin-metadata`**!

## Como funciona
Mesmo quando um app escrito em **Kotlin** foi ofuscado pelo ProGuard/R8, o compilador Kotlin frequentemente deixa a anotação **`@kotlin.Metadata`** intacta dentro das classes: o plugin `kotlin-metadata` do JADX (ativo por padrão!) lê o protobuf binário de `@kotlin.Metadata` e **recupera os nomes originais das funções, argumentos, propriedades, `data class` e `companion object`**!

## Exemplo
```bash
# Decompilar um APK ofuscado ativando o desofuscador automatico (--deobf), salvando o mapa .jobf e corrigindo colisoes de nomes
jadx -d /cases/mobile/app_deobfuscated \
  --deobf \
  --deobf-min 3 \
  --deobf-max 64 \
  --deobf-cfg-file /cases/mobile/target_app.jobf \
  --deobf-cfg-file-mode read-or-save \
  --rename-flags all \
  /cases/mobile/target_app.apk
```

## Limites e trade-offs
Veja como **`--use-kotlin-methods-for-var-names apply`** (ativo por padrão) ajuda na engenharia reversa de apps Kotlin: sempre que o compilador Kotlin insere chamadas `Intrinsics.checkNotNullParameter(p0, "userPassword")` no início de um método, o JADX lê a string `"userPassword"` e renomeia automaticamente a variável `p0` para `userPassword` no código decompilado!

## Como verificar
Se a equipe de desenvolvimento fornecer o arquivo `mapping.txt` gerado pelo R8 durante um pentest White-Box/Grey-Box, passe `-Prename-mappings.format=PROGUARD_FILE --mappings-path mapping.txt` para restaurar 100% dos nomes originais.

## Conexões
- [[jadx-modos-decompilacao-restructure-simple-fallback-show-bad-code]] — Veja também: JADX: Modos de Decompilação (**`-m auto | restructure | simple | fallback`**) e **`--show-bad-code`** para Métodos Ofuscados que Falham no AST.
- [[jadx-auditoria-androidmanifest-exported-components-deep-links-permissions]] — Veja também: Auditoria de Superfície de Ataque Android no JADX: **`AndroidManifest.xml`**, Componentes Exportados (`exported="true"`), **Intent Filters / Deep Links** e `allowBackup`.
- [[jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android]] — Referência cruzada direta com jadx-arquitetura-decompilador-dex-java-apk-aab-arsc-android.
- [[jadx-automacao-scripts-jadx-kts-plugins-transformacao-ast]] — Referência cruzada direta com jadx-automacao-scripts-jadx-kts-plugins-transformacao-ast.

## Fontes
- [JADX Official GitHub — Dex to Java Decompiler CLI & GUI Options Reference](https://raw.githubusercontent.com/skylot/jadx/master/README.md) — documentação oficial completa do JADX cobrindo opções de linha de comando, modos de decompilação, desofuscação, grafos CFG/Call-Graph e plugins Kotlin/mappings; consultado em 2026-10-03.
- [JADX Official Wiki — jadx-gui Features Overview & Security Analysis](https://github.com/skylot/jadx/wiki/jadx-gui-features-overview) — wiki oficial do JADX demonstrando navegação no AndroidManifest.xml, busca de referências, modo debug Smali e exclusão de pacotes; consultado em 2026-10-03.
