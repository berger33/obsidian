---
id: software.seguranca.tranche18.001748
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

# KubeLinter: Usar resultado como pre-merge gate

## Em uma frase
**KubeLinter — Usar resultado como pre-merge gate:** Um job de lint pode impedir merge quando encontra erro configurado, desde que o status do comando seja respeitado.

## Por que importa
O recorte de **usar resultado como pre-merge gate** ajuda a detectar configurações potencialmente inseguras durante revisão de manifests antes da aplicação. A equipe registra risco, evidência e responsável.

## Como funciona
Para **usar resultado como pre-merge gate**, o linter carrega arquivos, aplica checks selecionados e relata objeto, regra e orientação de remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute kube-linter em todos os manifests alterados e torne o status requerido no repositório. Teste em staging autorizado.

## Limites e trade-offs
Um job que usa `continue-on-error` pode exibir achados sem bloquear merge. Exceções exigem responsável e prazo.

## Como verificar
Introduza falha controlada em branch de teste e confirme bloqueio pela proteção de branch. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-linter-interpretar-objeto-e-orientacao-de-correcao]] — Complementa o tópico com kubelinter: interpretar objeto e orientação de correção.

## Fontes
- [KubeLinter — Project documentation](https://github.com/stackrox/kube-linter) — repositório oficial que descreve alvo, checks padrões e comandos do projeto; consultado em 2026-10-04.
- [KubeLinter — Configuring KubeLinter](https://github.com/stackrox/kube-linter/blob/main/docs/configuring-kubelinter.md) — referência oficial de configuração, checks, paths ignorados e checks customizados; consultado em 2026-10-04.
