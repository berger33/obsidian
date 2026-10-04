---
id: software.seguranca.tranche17.001690
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://github.com/aquasecurity/kube-bench", "https://aquasecurity.github.io/kube-bench/v0.6.6/controls/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# kube-bench: Exceções para plataforma gerenciada

## Em uma frase
**kube-bench — Exceções para plataforma gerenciada:** Serviços Kubernetes gerenciados podem ocultar controles ou assumir responsabilidade por partes do plano de controle.

## Por que importa
O recorte de **exceções para plataforma gerenciada** ajuda a verificar hardening de cluster e transformar recomendações documentadas em tarefas rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **exceções para plataforma gerenciada**, checks descritos em arquivos YAML executam auditorias locais ou comandos de configuração e comparam saída a critérios previstos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Marque controls fora de escopo somente com evidência do provedor e limite a exceção ao recurso gerenciado. Teste em staging autorizado.

## Limites e trade-offs
Assumir que provedor cobre controle sem contrato ou evidência deixa lacuna operacional. Exceções exigem responsável e prazo.

## Como verificar
Associe documentação do provedor, versão do serviço e responsável à decisão de aplicabilidade. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[asvs-fixar-versao-do-asvs-no-contrato]] — Complementa o tópico com owasp asvs: fixar versão do asvs no contrato.

## Fontes
- [Aqua kube-bench — Repository](https://github.com/aquasecurity/kube-bench) — repositório oficial e descrição da ferramenta CIS Kubernetes Benchmark; consultado em 2026-10-04.
- [Aqua kube-bench — Controls and YAML](https://aquasecurity.github.io/kube-bench/v0.6.6/controls/) — documentação versionada dos arquivos de controles, comandos de auditoria e critérios de checks; consultado em 2026-10-04.
