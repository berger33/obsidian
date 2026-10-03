---
id: software.devops.tranche09.000817
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
fontes: ["https://raw.githubusercontent.com/k3s-io/k3s/main/README.md", "https://docs.k3s.io/architecture", "https://github.com/k3s-io/k3s"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# K3s: gerenciamento automatizado e rotação de certificados TLS dos componentes com k3s certificate

## Em uma frase
O K3s automatiza a geração, renovação e rotação dos certificados TLS de todos os componentes internos do Kubernetes (`/var/lib/rancher/k3s/server/tls`) e fornece o subcomando `k3s certificate` (`check` e `rotate`) para inspeção e rotação sob demanda.

## Por que importa
Em clusters Kubernetes de longa duração (especialmente em lojas físicas, fábricas ou ambientes de borda que operam por anos), a expiração silenciosa dos certificados TLS internos do `kube-apiserver`, `etcd` ou `kubelet` derruba toda a comunicação do cluster se não houver renovação automática e ferramentas simples de auditoria. O README oficial do K3s cita o gerenciamento de certificados TLS como uma das principais simplificações operacionais da distribuição.

## Como funciona
Na inicialização do `k3s server`, o K3s gera automaticamente a hierarquia de autoridades certificadoras (CAs de cliente, servidor, request-header e etcd) e os certificados de folha em `/var/lib/rancher/k3s/server/tls` com validade padrão de 1 ano (e CAs de 10 anos). Sempre que um certificado está a menos de 120 dias (ou 90 dias, conforme a versão) de expirar, o K3s o renova automaticamente ao reiniciar o serviço ou em ciclo contínuo. Além disso, o administrador pode auditar a validade exata de cada certificado com **`sudo k3s certificate check`** e forçar a rotação manual imediata de todos os certificados de serviço com **`sudo k3s certificate rotate`** seguido do restart do serviço `k3s`.

## Exemplo
```bash
# Verificar a data de expiração e o status de todos os certificados TLS gerenciados pelo K3s no nó server
sudo k3s certificate check --output table
```

## Limites e trade-offs
Quando `sudo k3s certificate rotate` é executado para rotacionar os certificados dos componentes do servidor (ou `rotate-ca` para trocar as autoridades certificadoras), é obrigatório reiniciar o serviço `systemctl restart k3s` (e `k3s-agent` nos workers caso as CAs tenham mudado) para que os processos em memória carreguem os novos certificados do disco.

## Como verificar
Execute `sudo k3s certificate check` e confirme que todos os certificados em `/var/lib/rancher/k3s/server/tls/` apresentam status válido e janela de expiração saudável.

## Conexões
- [[k3s-auto-deploy-manifestos-helm-controller-crd]] — Veja também: K3s: auto-deploy em tempo real de manifestos em /var/lib/rancher/k3s/server/manifests e Helm-controller (CRD HelmChart).
- [[k3s-configuracao-config-yaml-systemd-desinstalacao-scripts]] — Veja também: K3s: configuração declarativa em /etc/rancher/k3s/config.yaml, serviços systemd e scripts de limpeza.
- [[k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura]] — Referência cruzada direta com k3s-distribuicao-kubernetes-leve-binario-unico-arquitetura.
- [[k3s-seguranca-identidade-nos-node-password-secrets-certificados]] — Referência cruzada direta com k3s-seguranca-identidade-nos-node-password-secrets-certificados.

## Fontes
- [K3s GitHub — README.md (Lightweight Kubernetes, Single Binary & Bundled Components)](https://raw.githubusercontent.com/k3s-io/k3s/main/README.md) — README oficial do K3s (projeto CNCF Sandbox) descrevendo o empacotamento em binário único com containerd, Flannel, CoreDNS, Traefik, Klipper ServiceLB, Spegel e Kine; consultado em 2026-10-03.
- [K3s Official Documentation — Architecture (Server/Agent Processes, Tunnel Proxy, Kine & Embedded etcd HA)](https://docs.k3s.io/architecture) — Documentação oficial de arquitetura do K3s explicando os processos k3s server e k3s agent, conexões WebSocket do Tunnel Proxy, alta disponibilidade com datastore externo (Kine) ou etcd embarcado e requisito de hostname único; consultado em 2026-10-03.
- [K3s Official Documentation — Quick-Start Guide](https://github.com/k3s-io/k3s) — Guia rápido oficial de instalação com get.k3s.io, K3S_URL, K3S_TOKEN e kubeconfig em /etc/rancher/k3s/k3s.yaml; consultado em 2026-10-03.
