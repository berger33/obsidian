---
id: software.seguranca.tranche17.001689
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

# kube-bench: Acesso e ambiente de execução

## Em uma frase
**kube-bench — Acesso e ambiente de execução:** Auditoria local pode exigir leitura de arquivos de host e acesso a componentes específicos.

## Por que importa
O recorte de **acesso e ambiente de execução** ajuda a verificar hardening de cluster e transformar recomendações documentadas em tarefas rastreáveis. A equipe registra risco, evidência e responsável.

## Como funciona
Para **acesso e ambiente de execução**, checks descritos em arquivos YAML executam auditorias locais ou comandos de configuração e comparam saída a critérios previstos. Delimite entrada e saída. Repita se o alvo mudar.

## Exemplo
Execute scanner em nó de laboratório com permissões mínimas necessárias e examine mounts/capabilities do container. Teste em staging autorizado.

## Limites e trade-offs
Imagem com privilégios amplos aumenta superfície e pode não funcionar em cluster gerenciado. Exceções exigem responsável e prazo.

## Como verificar
Revise manifesto do job e compare permissões com comandos de controle habilitados. Guarde versão e configuração. Inclua casos positivos e negativos.

## Conexões
- [[kube-bench-excecoes-para-plataforma-gerenciada]] — Complementa o tópico com kube-bench: exceções para plataforma gerenciada.

## Fontes
- [Aqua kube-bench — Repository](https://github.com/aquasecurity/kube-bench) — repositório oficial e descrição da ferramenta CIS Kubernetes Benchmark; consultado em 2026-10-04.
- [Aqua kube-bench — Controls and YAML](https://aquasecurity.github.io/kube-bench/v0.6.6/controls/) — documentação versionada dos arquivos de controles, comandos de auditoria e critérios de checks; consultado em 2026-10-04.
