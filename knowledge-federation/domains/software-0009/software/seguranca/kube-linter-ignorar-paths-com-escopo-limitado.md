---
id: software.seguranca.tranche18.001745
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

# KubeLinter: Ignorar paths com escopo limitado

## Em uma frase
**KubeLinter — Ignorar paths com escopo limitado:** `ignorePaths` pode excluir caminhos por padrão glob, permitindo remover fixtures ou arquivos irrelevantes.

## Por que importa
O recorte de **ignorar paths com escopo limitado** ajuda a detectar configurações potencialmente inseguras durante revisão de manifests antes da aplicação. A equipe registra risco, evidência e responsável.

## Como funciona
Para **ignorar paths com escopo limitado**, o linter carrega arquivos, aplica checks selecionados e relata objeto, regra e orientação de remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Exclua somente `vendor/generated/` se o diretório for comprovadamente gerado e nunca implantado. Teste em staging autorizado.

## Limites e trade-offs
Caminhos glob podem corresponder a mais arquivos após mudança de layout. Exceções exigem responsável e prazo.

## Como verificar
Liste arquivos efetivamente ignorados em uma revisão e cheque a exclusão no diff. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-linter-avaliar-charts-helm]] — Complementa o tópico com kubelinter: avaliar charts helm.

## Fontes
- [KubeLinter — Project documentation](https://github.com/stackrox/kube-linter) — repositório oficial que descreve alvo, checks padrões e comandos do projeto; consultado em 2026-10-04.
- [KubeLinter — Configuring KubeLinter](https://github.com/stackrox/kube-linter/blob/main/docs/configuring-kubelinter.md) — referência oficial de configuração, checks, paths ignorados e checks customizados; consultado em 2026-10-04.
