---
id: software.devops.tranche09.000804
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
fontes: ["https://raw.githubusercontent.com/siderolabs/talos/main/README.md", "https://docs.siderolabs.com/talos/v1.9/learn-more/philosophy", "https://github.com/siderolabs/talos"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Talos Linux: configuração declarativa unificada da máquina e do Kubernetes em um único manifesto YAML

## Em uma frase
No Talos Linux, toda a configuração tanto do sistema operacional da máquina (rede, discos, NTP, sysctls, certificados) quanto do cluster Kubernetes que ela forma é definida por um único arquivo YAML declarativo (`controlplane.yaml` ou `worker.yaml`), sem scripts procedurais.

## Por que importa
Em instalações tradicionais de Kubernetes, o operador precisa manter scripts Terraform/cloud-init para o SO, playbooks Ansible para instalar pacotes e arquivos separados do `kubeadm` para o cluster; quando uma etapa falha na metade, a máquina fica em estado inconsistente. Conforme destaca a seção `Declarative` da filosofia oficial do Talos, unificar tudo em um único YAML declarativo elimina passos procedurais e desvios.

## Como funciona
Usando o comando `talosctl gen config <nome-do-cluster> https://<endpoint>:6443`, o administrador gera os segredos PKI do cluster e os manifestos declarativos **`controlplane.yaml`**, **`worker.yaml`** e a configuração do cliente **`talosconfig`**. Um único arquivo `worker.yaml` pode frequentemente ser aplicado de forma idêntica a dezenas de máquinas workers (`talosctl apply-config --insecure -n <ip> --file worker.yaml`), e customizações específicas (como definir o disco de instalação, VIP da API ou patches de rede) são aplicadas de forma limpa via patches YAML/JSON (`--config-patch`) sem nunca editar scripts bash na máquina.

## Exemplo
```bash
# Gerar os manifestos declarativos (controlplane.yaml, worker.yaml e talosconfig) e aplicar a um nó novo
talosctl gen config prod-cluster https://10.0.0.100:6443
talosctl apply-config --insecure --nodes 10.0.0.10 --file controlplane.yaml
```

## Limites e trade-offs
A flag `--insecure` no comando `talosctl apply-config --insecure` só deve ser usada no momento do provisionamento inicial enquanto o nó está em modo de manutenção aguardando sua primeira configuração (antes de possuir as chaves mTLS do cluster); assim que a configuração inicial é aplicada, toda alteração subsequente deve usar `talosctl apply-config` autenticado por mTLS via `talosconfig`.

## Como verificar
Execute `talosctl -n <ip-do-no> get machineconfig -o yaml` para inspecionar a configuração declarativa ativa no nó e confirmar sua sincronização com o manifesto versionado no Git.

## Conexões
- [[talos-particoes-disco-camadas-rootfs-squashfs-overlayfs]] — Veja também: Talos Linux: layout das 6 partições de disco (EFI, BIOS, BOOT, META, STATE, EPHEMERAL) e 3 camadas de filesystem.
- [[talos-endurecimento-seguranca-kspp-modulos-kernel-mtls]] — Veja também: Talos Linux: endurecimento de segurança por padrão (KSPP, bloqueio de módulos dinâmicos de kernel e PKI mTLS rotativa).
- [[talos-linux-sistema-operacional-imutavel-api-kubernetes]] — Referência cruzada direta com talos-linux-sistema-operacional-imutavel-api-kubernetes.

## Fontes
- [Talos Linux Documentation — What is Talos (Immutability, Minimalism, Ephemerality & API-Driven Management)](https://raw.githubusercontent.com/siderolabs/talos/main/README.md) — Visão geral oficial do Talos Linux detalhando ausência de shell/SSH, cerca de 12 binários no sistema de arquivos, partições efêmeras criptografadas com KMS/TPM e recomendações CIS/NIST; consultado em 2026-10-03.
- [Talos Linux Documentation — Architecture & Design Philosophy (PID 1 machined, squashfs, udevd, containerd & COSI)](https://docs.siderolabs.com/talos/v1.9/learn-more/philosophy) — Documentação oficial de arquitetura e filosofia do Talos Linux explicando o binário init machined (PID 1), montagem do rootfs squashfs, serviços em containers containerd e sistema de recursos COSI; consultado em 2026-10-03.
- [Sidero Labs Talos — Official GitHub README.md](https://github.com/siderolabs/talos) — README oficial do repositório siderolabs/talos; consultado em 2026-10-03.
