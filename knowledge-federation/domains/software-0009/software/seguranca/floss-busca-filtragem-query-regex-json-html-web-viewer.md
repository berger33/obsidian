---
id: software.seguranca.tranche13.001236
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md", "https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Busca com Expressões Regulares (**`--query`**), Exportação **`-j` JSON** e Relatório Visual Interativo (**`--html`**) no FLOSS

## Em uma frase
Depois que o FLOSS extrai todas as strings estáticas, *stack*, *tight*, *decoded* e de *Go/Rust*, como pesquisar padrões específicos dentro desse universo unificado ou gerar um relatório interativo para compartilhar com a equipe de Resposta a Incidentes?

## Por que importa
O FLOSS disponibiliza três recursos nativos para consulta e geração de artefatos de análise: **(1) Busca Integrada (`--query <termo_ou_regex>`)** — pesquisa um texto literal ou uma expressão regular (com `--regex`) através de **todas as categorias de strings extraídas** (por exemplo, encontrar um domínio `.onion` mesmo que ele estivesse oculto como uma *Stack String* ou *Decoded String*!); **(2) Saída Estruturada JSON (`-j, --json`)** — exporta todas as strings com seus offsets, codificações (`ASCII`, `UTF-16LE`, `UTF-8`), endereços de funções e tags semânticas; e **(3) Relatório Visual Interativo (`--html relatorio_floss.html`)**!

## Como funciona
O arquivo gerado por **`--html`** é uma página HTML autocontida com busca instantânea, filtros por tipo de string, filtros por tags semânticas (`url`, `ip`, `registry`), ordenação por score de relevância e contexto de função!

## Exemplo
```bash
# Buscar via regex por URLs/IPs/chaves de registro em todas as strings desofuscadas e gerar um relatorio HTML interativo
floss --query "https?://|HKEY_|cmd\.exe|powershell" --regex ./amostras/loader.exe
floss --html ./relatorio_strings_loader.html ./amostras/loader.exe
```

## Limites e trade-offs
Dica de ouro para não retrabalhar: como a emulação de *Decoded Strings* e *Tight Strings* em um binário grande pode levar alguns segundos ou minutos, gere primeiro o JSON completo (**`floss -j amostra.exe > strings.json`**) e depois passe o próprio arquivo **`strings.json`** como entrada para o FLOSS (**`floss --interesting strings.json`** ou **`floss --html relatorio.html strings.json`**) — ele recarrega os resultados instantaneamente sem reanalisar o binário!

## Como verificar
Você também pode definir **`export FLOSS_CACHE_DIR=~/.cache/floss`** para que o FLOSS faça cache automático dos resultados por hash `SHA-256` das amostras analisadas.

## Conexões
- [[floss-layout-aware-static-strings-section-structure-semantic-tags]] — Veja também: Strings Estáticas Conscientes de Layout (**Layout-Aware Static Strings**) e **Tags Semânticas (`--tag`, `--interesting`)** no FLOSS.
- [[floss-integracao-ida-pro-ghidra-binary-ninja-relatorio-html]] — Veja também: Anotando Automaticamente Desmontadores (**IDA Pro, Ghidra, Binary Ninja e x64dbg**) com os Scripts Gerados pelo FLOSS.
- [[floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded]] — Referência cruzada direta com floss-arquitetura-extracao-strings-ofuscadas-stack-tight-decoded.

## Fontes
- [Mandiant FLARE Obfuscated String Solver (`flare-floss`) Official GitHub](https://raw.githubusercontent.com/mandiant/flare-floss/master/README.md) — repositório oficial do Mandiant FLOSS cobrindo extração de strings estáticas conscientes de layout, stack strings, tight strings, decoded strings e binários Go/Rust; consultado em 2026-10-03.
- [Mandiant FLOSS Official Usage Guide (`doc/usage.md`)](https://raw.githubusercontent.com/mandiant/flare-floss/master/doc/usage.md) — documentação oficial de opções avançadas do FLOSS (`--only`, `--no`, `--functions`, `--section`, `--structure`, `--tag`, `--interesting`, `--query`, `--html`, `-L` e `FLOSS_CACHE_DIR`); consultado em 2026-10-03.
