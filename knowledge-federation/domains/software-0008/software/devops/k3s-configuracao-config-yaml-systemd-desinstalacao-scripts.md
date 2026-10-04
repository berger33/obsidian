---
id: software.devops.tranche09.000818
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/k3s-io/k3s/main/README.md", "https://docs.k3s.io/quick-start", "https://github.com/k3s-io/k3s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K3s: configuração declarativa em /etc/rancher/k3s/config.yaml, serviços systemd e scripts de limpeza

## Em uma frase
O K3s permite declarar todas as flags de linha de comando do servidor ou agente no arquivo `/etc/rancher/k3s/config.yaml` (e diretório `config.yaml.d/`) e cria automaticamente os serviços `systemd`/`openrc` e os scripts de remoção completa (`k3s-uninstall.sh` e `k3s-killall.sh`).

## Por que importa
Passar dezenas de argumentos longos diretamente no comando `curl -sfL https://get.k3s.io | sh -s - ...` ou editar manualmente arquivos `.service` do `systemd` dificulta a manutenção e a leitura da configuração do nó por ferramentas de IaC (Ansible, Salt, cloud-init). A documentação oficial do K3s padroniza a configuração via `/etc/rancher/k3s/config.yaml`.

## Como funciona
Qualquer flag suportada pelo `k3s server` ou `k3s agent` (por exemplo, `--write-kubeconfig-mode 0644`, `--disable traefik`, `--tls-san k8s.exemplo.com`, `--node-label`) pode ser escrita como chave YAML sem os traços iniciais dentro de **`/etc/rancher/k3s/config.yaml`** antes mesmo de rodar o instalador `https://get.k3s.io`. Durante a instalação, o script configura o serviço `k3s.service` (ou `k3s-agent.service`) e instala em `/usr/local/bin/` três utilitários de ciclo de vida: (1) `k3s` (com links simbólicos para `kubectl`, `crictl` e `ctr`); (2) **`k3s-killall.sh`** (que para todos os containers K3s e desmonta volumes/redes sem desinstalar o K3s); e (3) **`k3s-uninstall.sh`** (ou `k3s-agent-uninstall.sh`, que remove completamente o K3s e seus dados do host).

## Exemplo
```yaml
# Exemplo de /etc/rancher/k3s/config.yaml substituindo flags complexas de linha de comando
write-kubeconfig-mode: "0640"
tls-san:
  - "k8s-api.interno.empresa.com"
disable:
  - traefik
node-label:
  - "topology.kubernetes.io/zone=edge-sp-01"
```

## Limites e trade-offs
O script `k3s-uninstall.sh` remove o serviço systemd, limpa as regras de iptables/CNI e **apaga permanentemente** o diretório `/var/lib/rancher/k3s` (incluindo o banco de dados SQLite ou `etcd` embutido e os volumes do `local-path-provisioner` armazenados ali); em ambientes de produção, faça sempre um snapshot do datastore antes de qualquer operação destrutiva no nó.

## Como verificar
Após editar `/etc/rancher/k3s/config.yaml` e executar `sudo systemctl restart k3s`, verifique com `sudo systemctl status k3s` e `sudo k3s kubectl get nodes --show-labels` que as configurações foram aplicadas.

## Conexões
- [[k3s-gerenciamento-certificados-tls-rotacao-operacoes]] — Veja também: K3s: gerenciamento automatizado e rotação de certificados TLS dos componentes com k3s certificate.
- [[k3s-instalacao-air-gap-imagens-tarball-registries-privados]] — Veja também: K3s: implantação offline (Air-Gap) com tarball de imagens em /var/lib/rancher/k3s/agent/images e registries.yaml.
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.
- [[k3s-componentes-embutidos-containerd-flannel-traefik-klipper]] — Referência cruzada direta com k3s-componentes-embutidos-containerd-flannel-traefik-klipper.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/quick-start) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
