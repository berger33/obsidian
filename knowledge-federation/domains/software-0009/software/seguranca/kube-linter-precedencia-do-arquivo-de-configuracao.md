---
id: software.seguranca.tranche18.001742
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-18.md"
fontes: ["https://github.com/stackrox/kube-linter", "https://github.com/stackrox/kube-linter/blob/main/docs/configuring-kubelinter.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# KubeLinter: Precedência do arquivo de configuração

## Em uma frase
**KubeLinter — Precedência do arquivo de configuração:** Na ausência de opção explícita, KubeLinter procura nomes de configuração definidos no diretório atual antes de usar defaults.

## Por que importa
O recorte de **precedência do arquivo de configuração** ajuda a detectar configurações potencialmente inseguras durante revisão de manifests antes da aplicação. A equipe registra risco, evidência e responsável.

## Como funciona
Para **precedência do arquivo de configuração**, o linter carrega arquivos, aplica checks selecionados e relata objeto, regra e orientação de remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Passe `--config` no CI para não depender de um arquivo acidental no working directory. Teste em staging autorizado.

## Limites e trade-offs
Mudar diretório de execução pode alterar configuração carregada sem mudança no repositório. Exceções exigem responsável e prazo.

## Como verificar
Imprima ou audite o caminho de configuração usado em cada job. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-linter-selecionar-checks-por-inclusao-e-exclusao]] — Complementa o tópico com kubelinter: selecionar checks por inclusão e exclusão.

## Fontes
- [KubeLinter — Project documentation](https://github.com/stackrox/kube-linter) — repositório oficial que descreve alvo, checks padrões e comandos do projeto; consultado em 2026-10-04.
- [KubeLinter — Configuring KubeLinter](https://github.com/stackrox/kube-linter/blob/main/docs/configuring-kubelinter.md) — referência oficial de configuração, checks, paths ignorados e checks customizados; consultado em 2026-10-04.
