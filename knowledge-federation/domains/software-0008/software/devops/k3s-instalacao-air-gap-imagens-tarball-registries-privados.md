---
id: software.devops.tranche09.000819
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

# K3s: implantação offline (Air-Gap) com tarball de imagens em /var/lib/rancher/k3s/agent/images e registries.yaml

## Em uma frase
Para ambientes desconectados da internet (Air-Gap), o K3s disponibiliza a cada release arquivos `k3s-airgap-images-<arch>.tar.zst` importados automaticamente de `/var/lib/rancher/k3s/agent/images/` pelo `containerd` embutido, além de espelhamento de registries via `/etc/rancher/k3s/registries.yaml`.

## Por que importa
Em fábricas, navios, subestações de energia, hospitais e data centers financeiros isolados da internet (casos de uso centrais de Edge e IoT destacados no README do K3s), os nós não conseguem acessar o Docker Hub nem `get.k3s.io` para baixar imagens do CoreDNS, Flannel, Metrics Server ou Pause container. O modelo Air-Gap nativo do K3s resolve isso sem exigir infraestrutura externa complexa.

## Como funciona
Cada release oficial no GitHub (`github.com/k3s-io/k3s/releases`) publica, ao lado do binário `k3s` (`amd64`, `arm64`, `armhf`), um arquivo comprimido **`k3s-airgap-images-<arch>.tar.zst`** (ou `.tar.gz`/`.tar`) contendo todas as imagens de container necessárias para inicializar o cluster. Quando o operador coloca qualquer tarball de imagens OCI dentro do diretório **`/var/lib/rancher/k3s/agent/images/`**, o `k3s` importa automaticamente todas as imagens do arquivo para o `containerd` local na partida do serviço. Adicionalmente, o arquivo **`/etc/rancher/k3s/registries.yaml`** permite configurar mirrors privados (`mirrors`), endpoints HTTP/HTTPS, autenticação e certificados CA customizados para o `containerd` embutido sem nunca editar manualmente o `config.toml` do containerd.

## Exemplo
```bash
# Preparar imagens air-gap do K3s no diretório vigiado pelo containerd embutido antes de iniciar o serviço
sudo mkdir -p /var/lib/rancher/k3s/agent/images/
sudo cp ./k3s-airgap-images-amd64.tar.zst /var/lib/rancher/k3s/agent/images/
INSTALL_K3S_SKIP_DOWNLOAD=true ./install.sh
```

## Limites e trade-offs
Ao usar o script `install.sh` em uma máquina sem internet, é obrigatório passar a variável **`INSTALL_K3S_SKIP_DOWNLOAD=true`** (tendo copiado previamente o binário `k3s` para `/usr/local/bin/k3s` com `chmod +x`), caso contrário o script tentará conectar ao GitHub para baixar o binário e falhará por falta de rede.

## Como verificar
Execute `sudo k3s crictl images` no nó air-gap após iniciar o serviço para confirmar que todas as imagens de sistema do K3s (`rancher/mirrored-pause`, `rancher/mirrored-coredns-coredns`, etc.) foram pré-carregadas a partir do tarball local.

## Conexões
- [[k3s-configuracao-config-yaml-systemd-desinstalacao-scripts]] — Veja também: K3s: configuração declarativa em /etc/rancher/k3s/config.yaml, serviços systemd e scripts de limpeza.
- [[k3s-remocao-in-tree-drivers-suporte-csi-ccm-conformidade]] — Veja também: K3s: remoção de drivers in-tree legados, adoção de CSI e CCM out-of-tree e conformidade CNCF.
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.
- [[k3s-componentes-embutidos-containerd-flannel-traefik-klipper]] — Referência cruzada direta com k3s-componentes-embutidos-containerd-flannel-traefik-klipper.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/quick-start) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
