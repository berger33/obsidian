---
id: software.seguranca.tranche18.001731
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
fontes: ["https://kubescape.io/docs/scanning/", "https://kubescape.io/docs/frameworks-and-controls/frameworks/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Kubescape: Selecionar framework explicitamente

## Em uma frase
**Kubescape — Selecionar framework explicitamente:** Frameworks reúnem controles com escopo e versão definidos, como guias de hardening e benchmarks publicados.

## Por que importa
O recorte de **selecionar framework explicitamente** ajuda a encontrar desvios de configuração antes e depois da implantação com resultados ligados a recursos e controles. A equipe registra risco, evidência e responsável.

## Como funciona
Para **selecionar framework explicitamente**, o operador escolhe origem, framework ou control, executa o scan e revisa evidências antes de aplicar remediação. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute um framework identificado em manifests de staging e registre a versão selecionada. Teste em staging autorizado.

## Limites e trade-offs
Frameworks diferentes podem cobrir recursos distintos e produzir scores não comparáveis. Exceções exigem responsável e prazo.

## Como verificar
Guarde nome do framework e lista de controles junto do resultado de cada execução. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kubescape-executar-scan-de-um-control]] — Complementa o tópico com kubescape: executar scan de um control.

## Fontes
- [Kubescape — Scanning](https://kubescape.io/docs/scanning/) — documentação oficial de scans de cluster, arquivos, controls, score e exceções; consultado em 2026-10-04.
- [Kubescape — Frameworks](https://kubescape.io/docs/frameworks-and-controls/frameworks/) — catálogo oficial de frameworks e controles de segurança; consultado em 2026-10-04.
