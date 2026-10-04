---
id: software.devops.tranche17.001677
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-17.md"
fontes: ["https://docs.rke2.io/architecture", "https://raw.githubusercontent.com/rancher/rke2/master/README.md", "https://github.com/rancher/rke2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# RKE2: transição de Ingress NGINX (EOL em março de 2026) para Traefik como Ingress Controller padrão no RKE2 v1.36+

## Em uma frase
Em alinhamento com a aposentadoria (*End-of-Life*) do projeto comunitário Ingress NGINX anunciada pelo Kubernetes para março de 2026, o RKE2 adotou o **Traefik** como Ingress Controller padrão para novos clusters a partir da série **v1.36** (`v1.36.x+rke2r1`).

## Por que importa
Continuar implantando novos clusters de produção dependendo de um controlador de Ingress aposentado upstream expõe a borda do cluster a CVEs futuros sem patch de manutenção.

## Como funciona
No RKE2 v1.36+, novos clusters provisionam automaticamente o chart `rke2-traefik` via `helm-controller`. Para clusters existentes criados em versões anteriores que ainda utilizam `rke2-ingress-nginx`, a documentação oficial do RKE2 fornece um guia estruturado de migração para instalar o Traefik lado a lado, migrar as rotas de `Ingress` e descomissionar o NGINX com segurança.

## Exemplo
```yaml
# Customizando o rke2-traefik via HelmChartConfig:
apiVersion: helm.cattle.io/v1
kind: HelmChartConfig
metadata:
  name: rke2-traefik
  namespace: kube-system
spec:
  valuesContent: |-
    ports:
      websecure:
        tls:
          enabled: true
```

## Limites e trade-offs
Conforme documentado na arquitetura do RKE2, todos os componentes empacotados são compilados e ligados estaticamente com `Go+BoringCrypto`, com exceção explícita do Traefik.

## Como verificar
Verifique os controladores de Ingress ativos no cluster com `kubectl get ingressclass` e `kubectl get pods -n kube-system | grep -E "traefik|ingress-nginx"`.

## Conexões
- [[rke2-helm-controller-manifests-helmchartconfig-customizacao-addons]] — Veja também: RKE2: gerenciamento declarativo de add-ons via `helm-controller` e customização com `HelmChartConfig`.
- [[rke2-cis-hardening-profile-selinux-mcs-pod-security]] — Veja também: RKE2: endurecimento CIS Kubernetes Benchmark (`profile: cis`) e isolamento SELinux Multi-Category Security (MCS).

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://docs.rke2.io/architecture) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
