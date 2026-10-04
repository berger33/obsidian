---
id: software.seguranca.tranche18.001744
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

# KubeLinter: Criar checks customizados a partir de templates

## Em uma frase
**KubeLinter — Criar checks customizados a partir de templates:** Checks customizados podem reutilizar templates fornecidos e parâmetros como rótulos obrigatórios.

## Por que importa
O recorte de **criar checks customizados a partir de templates** ajuda a detectar configurações potencialmente inseguras durante revisão de manifests antes da aplicação. A equipe registra risco, evidência e responsável.

## Como funciona
Para **criar checks customizados a partir de templates**, o linter carrega arquivos, aplica checks selecionados e relata objeto, regra e orientação de remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Exija uma annotation de responsável para workloads de laboratório por meio de check customizado. Teste em staging autorizado.

## Limites e trade-offs
Check criado pela equipe pode estar errado ou interpretar recursos de forma incompleta. Exceções exigem responsável e prazo.

## Como verificar
Teste manifests que devem passar e falhar e revise a mensagem de remediação. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-linter-ignorar-paths-com-escopo-limitado]] — Complementa o tópico com kubelinter: ignorar paths com escopo limitado.

## Fontes
- [KubeLinter — Project documentation](https://github.com/stackrox/kube-linter) — repositório oficial que descreve alvo, checks padrões e comandos do projeto; consultado em 2026-10-04.
- [KubeLinter — Configuring KubeLinter](https://github.com/stackrox/kube-linter/blob/main/docs/configuring-kubelinter.md) — referência oficial de configuração, checks, paths ignorados e checks customizados; consultado em 2026-10-04.
