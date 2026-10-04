---
id: software.seguranca.tranche18.001750
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

# KubeLinter: Distinguir lint de avaliação de runtime

## Em uma frase
**KubeLinter — Distinguir lint de avaliação de runtime:** O linter julga YAML e chart, não prova como admission, RBAC, rede ou filesystem serão configurados no cluster.

## Por que importa
O recorte de **distinguir lint de avaliação de runtime** ajuda a detectar configurações potencialmente inseguras durante revisão de manifests antes da aplicação. A equipe registra risco, evidência e responsável.

## Como funciona
Para **distinguir lint de avaliação de runtime**, o linter carrega arquivos, aplica checks selecionados e relata objeto, regra e orientação de remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Combine lint de manifest com teste de admission e inspeção de pod efetivamente criado. Teste em staging autorizado.

## Limites e trade-offs
Um manifest limpo pode ser alterado por webhook ou valores de deploy. Exceções exigem responsável e prazo.

## Como verificar
Compare a configuração renderizada, objeto admitido e estado observado no cluster. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[tetragon-escolher-hook-point-da-policy]] — Complementa o tópico com cilium tetragon: escolher hook point da policy.

## Fontes
- [KubeLinter — Project documentation](https://github.com/stackrox/kube-linter) — repositório oficial que descreve alvo, checks padrões e comandos do projeto; consultado em 2026-10-04.
- [KubeLinter — Configuring KubeLinter](https://github.com/stackrox/kube-linter/blob/main/docs/configuring-kubelinter.md) — referência oficial de configuração, checks, paths ignorados e checks customizados; consultado em 2026-10-04.
