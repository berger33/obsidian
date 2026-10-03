---
id: software.devops.tranche15.001418
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md", "https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md", "https://github.com/sustainable-computing-io/kepler"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Kepler: implantação via Helm OCI, Kustomize, Kepler Operator e alinhamento estrito entre manifesto e imagem

## Em uma frase
O Kepler pode ser implantado em Kubernetes via Helm chart em registro OCI (`oci://quay.io/sustainable_computing_io/charts/kepler`), via Kustomize (`manifests/k8s`) ou pelo Kepler Operator, exigindo alinhamento exato entre a tag do repositório Git e a tag da imagem de container.

## Por que importa
Misturar manifestos da branch `main` com uma imagem de release anterior é uma armadilha operacional documentada que causa `CrashLoopBackOff` imediato devido a mudanças nos endpoints de healthcheck (como `/probe/livez` e `/probe/readyz`).

## Como funciona
Ao implantar com Kustomize, o administrador deve sempre executar `git checkout <tag>` (por exemplo `v0.11.4`) antes de renderizar `kubectl kustomize manifests/k8s` e substituir `<KEPLER_IMAGE>` exatamente pela mesma versão `quay.io/sustainable_computing_io/kepler:v0.11.4`, aplicando com `--server-side --force-conflicts`.

## Exemplo
```bash
git checkout v0.11.4
kubectl kustomize manifests/k8s | \
  sed -e "s|<KEPLER_IMAGE>|quay.io/sustainable_computing_io/kepler:v0.11.4|g" | \
  kubectl apply --server-side --force-conflicts -f -
```

## Limites e trade-offs
Nunca aplique `manifests/k8s` diretamente do topo da branch `main` apontando para uma imagem estável antiga, pois probes de liveness e flags recém-adicionadas no manifesto não existirão no binário da imagem.

## Como verificar
Verifique a saúde dos Pods com `kubectl get pods -n kepler` e confirme que os endpoints de probe respondem sem reinicializações nos containers.

## Conexões
- [[kepler-reducao-privilegios-seguranca-readonly-proc-sys-sem-cap-bpf]] — Veja também: Kepler: endurecimento de segurança na série v0.10+ com acesso somente leitura a `/proc` e `/sys`.
- [[kepler-calculo-kwh-intensidade-carbono-promql-greenops]] — Veja também: Kepler: conversão de Joules para kWh e cálculo de pegada de carbono em consultas PromQL.

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
