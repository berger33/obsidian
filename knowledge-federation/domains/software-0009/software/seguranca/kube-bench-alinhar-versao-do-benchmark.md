---
id: software.seguranca.tranche17.001681
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

# kube-bench: Alinhar versão do benchmark

## Em uma frase
**kube-bench — Alinhar versão do benchmark:** A escolha do benchmark CIS precisa corresponder ao perfil e versão de Kubernetes auditados.

## Por que importa
O recorte de **alinhar versão do benchmark** ajuda a verificar hardening de cluster e transformar recomendações documentadas em tarefas rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **alinhar versão do benchmark**, checks descritos em arquivos YAML executam auditorias locais ou comandos de configuração e comparam saída a critérios previstos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Rode auditoria em cluster de teste após upgrade e indique benchmark correspondente à versão do servidor. Teste em staging autorizado.

## Limites e trade-offs
Comparação com benchmark de outra versão pode reportar divergências não aplicáveis. Exceções exigem responsável e prazo.

## Como verificar
Guarde versão do kube-bench, Kubernetes e benchmark no relatório de auditoria. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-bench-separar-checks-por-papel-do-no]] — Complementa o tópico com kube-bench: separar checks por papel do nó.

## Fontes
- [Aqua kube-bench — Repository](https://github.com/aquasecurity/kube-bench) — repositório oficial e descrição da ferramenta CIS Kubernetes Benchmark; consultado em 2026-10-04.
- [Aqua kube-bench — Controls and YAML](https://aquasecurity.github.io/kube-bench/v0.6.6/controls/) — documentação versionada dos arquivos de controles, comandos de auditoria e critérios de checks; consultado em 2026-10-04.
