---
id: software.devops.tranche09.000806
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
fontes: ["https://raw.githubusercontent.com/siderolabs/talos/main/README.md", "https://docs.siderolabs.com/talos/v1.9/learn-more/architecture", "https://github.com/siderolabs/talos"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Talos Linux: atualizações atômicas baseadas em imagem (talosctl upgrade) e reset limpo de nós (talosctl reset)

## Em uma frase
Como o Talos Linux distribui o sistema operacional inteiro como uma imagem SquashFS única e versionada, atualizações do SO (`talosctl upgrade`) ocorrem de forma atômica trocando a imagem de boot (com fallback automático A/B), e a reciclagem do nó ocorre via `talosctl reset`.

## Por que importa
Atualizar o sistema operacional de nós Kubernetes tradicionais com `apt-get dist-upgrade` ou `yum update` modifica centenas de pacotes individualmente no disco ativo, podendo deixar o nó incapaz de dar boot ou com bibliotecas incompatíveis entre diferentes nós do mesmo cluster. O README e a documentação de arquitetura do Talos destacam as atualizações atômicas e a velocidade de reconstrução de máquinas.

## Como funciona
Durante um **`talosctl upgrade --nodes <ip> --image ghcr.io/siderolabs/installer:<versao>`**, o Talos faz cordon/drain do nó Kubernetes, baixa a nova imagem unificada (contendo kernel Linux, `initramfs` e imagem SquashFS do `rootfs`), grava na partição `BOOT` secundária (esquema A/B), preserva os dados de `STATE` e `EPHEMERAL` (`/var`, mantendo dados do `etcd` e cache de imagens) e reinicia o nó na nova versão; caso o boot na nova versão falhe, o bootloader reverte automaticamente para a entrada anterior funcional. Já o comando **`talosctl reset`** drena/remove o nó do cluster e limpa as partições (ou seletivamente via `--system-labels-to-wipe STATE,EPHEMERAL`) para descomissionar ou reprovisionar o servidor do zero em poucos instantes.

## Exemplo
```bash
# Executar upgrade atômico de um nó Talos para uma nova versão do instalador e verificar saúde pós-boot
talosctl upgrade --nodes 10.0.0.10 --image ghcr.io/siderolabs/installer:v1.9.0
talosctl health --nodes 10.0.0.10
```

## Limites e trade-offs
Em nós de control plane que hospedam membros do banco de dados `etcd`, nunca dispare `talosctl upgrade` ou `talosctl reset` em todos os nós de control plane simultaneamente em paralelo; atualize sempre um nó de control plane por vez aguardando `talosctl health` confirmar que o membro do `etcd` voltou saudável ao quórum antes de prosseguir para o próximo nó.

## Como verificar
Execute `talosctl health --nodes <ip-control-plane>` antes e depois de cada `talosctl upgrade` para confirmar que o `etcd`, a API do Kubernetes, o `kubelet` e todos os nós estão saudáveis.

## Conexões
- [[talos-endurecimento-seguranca-kspp-modulos-kernel-mtls]] — Veja também: Talos Linux: endurecimento de segurança por padrão (KSPP, bloqueio de módulos dinâmicos de kernel e PKI mTLS rotativa).
- [[talos-bootstrap-etcd-gerenciamento-control-plane-ha]] — Veja também: Talos Linux: bootstrap do cluster Kubernetes, gerenciamento nativo do etcd e recuperação de quórum via talosctl.
- [[talos-linux-sistema-operacional-imutavel-api-kubernetes]] — Referência cruzada direta com talos-linux-sistema-operacional-imutavel-api-kubernetes.
- [[talos-particoes-disco-camadas-rootfs-squashfs-overlayfs]] — Referência cruzada direta com talos-particoes-disco-camadas-rootfs-squashfs-overlayfs.

## Fontes
- [Talos Linux Documentation — What is Talos (Immutability, Minimalism, Ephemerality & API-Driven Management)](https://raw.githubusercontent.com/siderolabs/talos/main/README.md) — Visão geral oficial do Talos Linux detalhando ausência de shell/SSH, cerca de 12 binários no sistema de arquivos, partições efêmeras criptografadas com KMS/TPM e recomendações CIS/NIST; consultado em 2026-10-03.
- [Talos Linux Documentation — Architecture & Design Philosophy (PID 1 machined, squashfs, udevd, containerd & COSI)](https://docs.siderolabs.com/talos/v1.9/learn-more/architecture) — Documentação oficial de arquitetura e filosofia do Talos Linux explicando o binário init machined (PID 1), montagem do rootfs squashfs, serviços em containers containerd e sistema de recursos COSI; consultado em 2026-10-03.
- [Sidero Labs Talos — Official GitHub README.md](https://github.com/siderolabs/talos) — README oficial do repositório siderolabs/talos; consultado em 2026-10-03.
