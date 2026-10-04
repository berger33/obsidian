---
id: software.devops.tranche17.001673
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
fontes: ["https://raw.githubusercontent.com/rancher/rke2/master/README.md", "https://docs.rke2.io/architecture", "https://github.com/rancher/rke2"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# RKE2: configuração declarativa em `/etc/rancher/rke2/config.yaml` e regras de precedência com flags CLI

## Em uma frase
Por rodar como serviço systemd (`rke2-server.service` ou `rke2-agent.service`), o RKE2 é configurado primariamente pelo arquivo YAML `/etc/rancher/rke2/config.yaml` (e arquivos drop-in em `/etc/rancher/rke2/config.yaml.d/`), onde cada flag da CLI mapeia diretamente para uma chave YAML.

## Por que importa
Editar arquivos de unit do systemd (`/etc/systemd/system/rke2-server.service`) para passar dezenas de flags de linha de comando dificulta a automação por Ansible/Cloud-Init e pode ser sobrescrito em atualizações de pacote.

## Como funciona
No `/etc/rancher/rke2/config.yaml`, flags simples viram pares chave-valor (`write-kubeconfig-mode: "0644"`) e flags repetíveis viram listas YAML (`tls-san`, `node-label`, `node-taint`). É possível combinar `config.yaml` com argumentos CLI, sabendo que argumentos CLI têm precedência e que, para argumentos repetíveis (como `--node-label`), passar a flag na CLI sobrescreve toda a lista definida no YAML.

## Exemplo
```yaml
# /etc/rancher/rke2/config.yaml
write-kubeconfig-mode: "0640"
tls-san:
  - "k8s-api.corp.internal"
  - "10.20.30.40"
node-label:
  - "tier=control-plane"
  - "compliance=fips"
cni:
  - "cilium"
```

## Limites e trade-offs
O caminho do arquivo de configuração pode ser alterado via flag `--config FILE` (`-c FILE`) ou variável de ambiente `$RKE2_CONFIG_FILE` caso seja necessário usar um layout fora de `/etc/rancher/rke2/config.yaml`.

## Como verificar
Valide a sintaxe do `/etc/rancher/rke2/config.yaml`, reinicie `systemctl restart rke2-server` e verifique nos certificados e labels do nó que `tls-san` e `node-label` foram aplicados.

## Conexões
- [[rke2-content-bootstrap-rke2-runtime-data-key-airgap-tarballs]] — Veja também: RKE2: processo de *Content Bootstrap* a partir da imagem `rancher/rke2-runtime` e tarballs air-gapped.
- [[rke2-sequencia-boot-server-agent-static-pods-etcd-apiserver]] — Veja também: RKE2: coreografia de inicialização de `server` e `agent` via goroutines e Static Pods.

## Fontes
- [RKE2 GitHub — README.md (Rancher's Next-Gen Kubernetes Distribution / RKE Government, FIPS 140-2, CIS Hardening & Configuration File)](https://raw.githubusercontent.com/rancher/rke2/master/README.md) — README oficial do rancher/rke2 detalhando conformidade FIPS 140-2 com Go+BoringCrypto, CIS Benchmark, instalação systemd e /etc/rancher/rke2/config.yaml; consultado em 2026-10-03.
- [RKE2 Official Documentation — Architecture (Content Bootstrap from rke2-runtime, Server/Agent Static Pod Lifecycle, CNI, Traefik & CIS/SELinux)](https://docs.rke2.io/architecture) — Documentação oficial de arquitetura do RKE2 explicando Content Bootstrap, Static Pods do control plane, helm-controller, plugins CNI e transição para Traefik v1.36+; consultado em 2026-10-03.
- [RKE2 — Official GitHub Repository](https://github.com/rancher/rke2) — Repositório oficial Apache-2.0 do Rancher RKE2; consultado em 2026-10-03.
