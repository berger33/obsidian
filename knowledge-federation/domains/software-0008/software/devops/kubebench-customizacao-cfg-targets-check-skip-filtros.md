---
id: software.devops.tranche13.001216
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md", "https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md", "https://github.com/aquasecurity/kube-bench"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Aqua kube-bench: Seleção de Alvos (--targets), Filtros de Controles (--check, --skip) e Customização de /opt/kube-bench/cfg

## Em uma frase
O `kube-bench` permite selecionar exatamente quais grupos de testes executar (`--targets master,node,etcd,policies`), focar em controles específicos (`--check 1.2.1,1.2.2`), pular controles inaplicáveis documentados (`--skip`) e montar arquivos YAML customizados sobre `/opt/kube-bench/cfg/`.

## Por que importa
Em distribuições Kubernetes customizadas onde o arquivo `kubelet.conf` ou o diretório de PKI fica em um caminho não-padrão (por exemplo, `/var/lib/rancher/k3s` ou `/var/snap/microk8s`), o arquivo `config.yaml` padrão precisa ser ajustado para localizar os binários e configurações reais.

## Como funciona
Montando um `ConfigMap` ou arquivo local `-v path/to/my-config.yaml:/opt/kube-bench/cfg/config.yaml:ro`, o operador adapta as listas de caminhos de binários e arquivos de configuração por componente sem alterar a lógica do executável Go.

## Exemplo
```bash
docker run --rm --pid=host \
  -v /etc:/etc:ro -v /var:/var:ro \
  docker.io/aquasec/kube-bench:latest \
  run --targets node --nosummary --noremediations
```

## Limites e trade-offs
Usar `--skip` de forma ampla para silenciar falhas `[FAIL]` no pipeline sem registrar justificativa técnica de compensação invalida o relatório de auditoria perante equipes de segurança.

## Como verificar
Documente qualquer controle ignorado ou caminho customizado em um `ConfigMap` versionado no Git e revise periodicamente todos os itens marcados como `[WARN]` e `[FAIL]`.

## Conexões
- [[kubebench-disa-stig-eks-conformidade-governamental]] — Veja também: Aqua kube-bench: Varredura de Conformidade DISA STIG em Clusters Kubernetes e EKS (job-eks-stig.yaml).
- [[kubebench-saida-json-junit-exit-code-automacao-ci-cronjob]] — Veja também: Aqua kube-bench: Exportação de Relatórios em JSON e JUnit (--json, --junit) e Uso em CronJobs de Auditoria.

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
