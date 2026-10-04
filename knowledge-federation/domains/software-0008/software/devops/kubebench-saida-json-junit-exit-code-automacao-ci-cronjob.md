---
id: software.devops.tranche13.001217
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
fontes: ["https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md", "https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md", "https://github.com/aquasecurity/kube-bench"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Aqua kube-bench: Exportação de Relatórios em JSON e JUnit (--json, --junit) e Uso em CronJobs de Auditoria

## Em uma frase
Para integrar a verificação do CIS Kubernetes Benchmark a pipelines de validação de infraestrutura e painéis de segurança, o `kube-bench` suporta saída estruturada em JSON (`--json`), formato de testes JUnit XML (`--junit`), gravação em arquivo (`--outputfile`) e controle de código de saída (`--exit-code`).

## Por que importa
Analisar logs de texto colorido com códigos ANSI manualmente após cada atualização de AMI de nó ou mudança no `kubeadm-config` não escala em frotas com dezenas de clusters.

## Como funciona
Ao executar `kube-bench run --json --outputfile /tmp/cis-report.json`, o relatório estrutura os contadores `total_pass`, `total_fail`, `total_warn` e `total_info` por seção, permitindo que um script ou coletor valide se `total_fail == 0` para os controles obrigatórios antes de promover um novo template de nó para produção.

## Exemplo
```bash
docker run --rm --pid=host -v /etc:/etc:ro -v /var:/var:ro \
  docker.io/aquasec/kube-bench:latest \
  run --targets node --json | jq '{total_pass, total_fail, total_warn, total_info}'
```

## Limites e trade-offs
Configurar `--exit-code 1` em um `Job` Kubernetes com `restartPolicy: OnFailure` faz com que o Kubernetes reinicie o Pod de auditoria repetidamente em loop sempre que houver um único controle `[FAIL]` no nó.

## Como verificar
Use `restartPolicy: Never` nos Jobs do `kube-bench` ou deixe o código de saída padrão (`0`) e avalie o campo `total_fail` do JSON no coletor de relatórios.

## Conexões
- [[kubebench-customizacao-cfg-targets-check-skip-filtros]] — Veja também: Aqua kube-bench: Seleção de Alvos (--targets), Filtros de Controles (--check, --skip) e Customização de /opt/kube-bench/cfg.
- [[kubebench-controles-kubelet-anonymous-auth-webhook-read-only-port]] — Veja também: Aqua kube-bench: Auditoria e Endurecimento do Kubelet (Seção 4: anonymous-auth, authorization-mode e read-only-port).

## Fontes
- [Aqua Security kube-bench GitHub — README.md (CIS Kubernetes Benchmark Checks, YAML Configs & Installation)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/README.md) — README oficial do aquasecurity/kube-bench explicando a execução dos testes do CIS Kubernetes Benchmark definidos em arquivos YAML por versão e distribuição; consultado em 2026-10-03.
- [kube-bench Official Documentation — Running kube-bench (Kubernetes Job, EKS/GKE/AKS/OCP Targets, Exit Codes & Mapping)](https://raw.githubusercontent.com/aquasecurity/kube-bench/main/docs/running.md) — Documentação oficial de execução do kube-bench detalhando job.yaml com hostPID, alvos específicos de provedores (--benchmark gke-1.2.0, eks-1.0.1, rh-1.0), flags de saída e mapeamento de versões; consultado em 2026-10-03.
- [Aqua Security kube-bench — Official GitHub Repository](https://github.com/aquasecurity/kube-bench) — Repositório oficial Apache-2.0 do kube-bench; consultado em 2026-10-03.
