---
id: software.devops.tranche15.001417
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

# Kepler: endurecimento de segurança na série v0.10+ com acesso somente leitura a `/proc` e `/sys`

## Em uma frase
A arquitetura moderna do Kepler (`0.10.0+`) eliminou a necessidade de capabilities privilegiadas de kernel como `CAP_SYSADMIN` e `CAP_BPF`, operando apenas com acesso somente leitura aos sistemas de arquivos `/proc` e `/sys` do host.

## Por que importa
Em clusters corporativos regidos por políticas estritas de segurança (Pod Security Standards, Gatekeeper ou Kyverno), conceder `CAP_SYSADMIN` ou `privileged: true` a um DaemonSet de métricas de energia frequentemente bloqueava a homologação junto à equipe de segurança.

## Como funciona
Ao ler contadores de energia diretamente da interface `powercap`/RAPL em `/sys/class/powercap` e estatísticas de cgroups/processos em `/proc` em modo *read-only*, o DaemonSet do Kepler coleta telemetria energética precisa sem carregar programas no kernel e sem capacidade de alterar o estado do sistema hospedeiro.

## Exemplo
```bash
kubectl get daemonset kepler -n kepler -o jsonpath='{.spec.template.spec.containers[0].securityContext}'
kubectl get daemonset kepler -n kepler -o jsonpath='{.spec.template.spec.volumes}'
```

## Limites e trade-offs
Embora o Kepler não exija mais `CAP_SYSADMIN`, as permissões de arquivo de `/sys/class/powercap/intel-rapl/*/energy_uj` em alguns kernels Linux recentes são restritas a `0400` (`root`), exigindo que o processo leitor tenha permissão de leitura sobre esses arquivos no host.

## Como verificar
Inspecione o `securityContext` e os `volumeMounts` do Pod do Kepler no namespace `kepler` e confirme que `/proc` e `/sys` estão montados com `readOnly: true`.

## Conexões
- [[kepler-metricas-processos-maquinas-virtuais-kvm-kubevirt]] — Veja também: Kepler: visibilidade energética por processo Linux (`kepler_process_*`) e máquinas virtuais (`kepler_vm_*`).
- [[kepler-implantacao-helm-oci-kustomize-alinhamento-tag-probes]] — Veja também: Kepler: implantação via Helm OCI, Kustomize, Kepler Operator e alinhamento estrito entre manifesto e imagem.

## Fontes
- [Kepler GitHub — README.md (v0.10.0+ Ground-Up Rewrite, Reduced Security Requirements, Dynamic RAPL Detection, Helm OCI & Kustomize Deployment)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/README.md) — README oficial do sustainable-computing-io/kepler detalhando a reescrita v0.10.0+, remoção de CAP_SYSADMIN/CAP_BPF, acesso somente leitura a /proc e /sys e métodos de instalação; consultado em 2026-10-03.
- [Kepler Official Documentation — docs/user/metrics.md (RAPL Energy Zones, Node, Container, Process & Virtual Machine Prometheus Metrics)](https://raw.githubusercontent.com/sustainable-computing-io/kepler/main/docs/user/metrics.md) — Referência oficial de métricas Prometheus do Kepler cobrindo zonas RAPL (psys, package, core, uncore, dram) e métricas em Joules e Watts para CPU e GPU; consultado em 2026-10-03.
- [Kepler — Official GitHub Repository](https://github.com/sustainable-computing-io/kepler) — Repositório oficial Apache-2.0 do Kepler na CNCF; consultado em 2026-10-03.
