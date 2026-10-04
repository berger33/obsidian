---
id: software.seguranca.tranche15.001426
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-15.md"
fontes: ["https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md", "https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Auditoria Offline de **Containers (`oscap-podman` / `oscap-docker`)**, Sistemas de Arquivos Montados (**`oscap-chroot`**) e Imagens de VM (**`oscap-vm` `qcow2`**)

## Em uma frase
Como auditar a conformidade de segurança e as vulnerabilidades CVE de uma **imagem de container OCI/Docker**, de um **disco virtual de VM (`qcow2` / `vmdk` / `raw`)** ou de uma partição montada **antes** mesmo de colocar o container ou a máquina virtual para rodar em produção?

## Por que importa
O OpenSCAP inclui wrappers oficiais especializados para inspeção *Offline / Agentless* de imagens: **(1) `oscap-podman` (e `oscap-docker`)** — monta o filesystem da imagem de container ou container em execução e avalia o Data Stream XCCDF/OVAL aplicando automaticamente as verificações de plataforma de container (ignorando regras que só fazem sentido em bare-metal, como particionamento de disco ou bootloader GRUB!).

## Como funciona
**(2)`oscap-chroot /mnt/rootfs`** — audita qualquer árvore de diretórios montada; e **(3) `oscap-vm image <disco.qcow2>`** (usa `libguestfs` para montar a imagem de disco da VM em modo somente-leitura e escaneá-la de fora!)!

## Exemplo
```bash
# Auditar offline uma imagem de container local com oscap-podman e um rootfs montado com oscap-chroot gerando relatorio HTML
oscap-podman imagem-app-producao:1.4.0 xccdf eval \
  --profile xccdf_org.ssgproject.content_profile_standard \
  --report ./relatorio-container.html /usr/share/xml/scap/ssg/content/ssg-rhel9-ds.xml
```

## Limites e trade-offs
Conforme explicado na documentação do `ComplianceAsCode/content`, os Data Streams modernos utilizam **Platform Checks (`CPE`)** em cada regra: quando você escaneia uma imagem de container com `oscap-podman` ou `oscap-chroot`, regras exclusivas de máquina física/VM (como `mount_option_var_tmp_noexec` ou `grub2_enable_iommu_force`) recebem automaticamente o status **`notapplicable`**!

## Como verificar
Coloque o `oscap-podman` ou `oscap-chroot` como um *Quality Gate* no seu pipeline de build de imagens de container e de imagens Packer (`qcow2` / AMI) para barrar imagens fora do padrão de hardening antes do push para o Registry.

## Conexões
- [[openscap-varredura-vulnerabilidades-cve-oval-eval-security-feeds]] — Veja também: Varredura de Vulnerabilidades de Pacotes (**CVE Scanning**) com **`oscap oval eval`**: Avaliando Feeds OVAL Oficiais (Red Hat, Ubuntu, Debian, SUSE, AlmaLinux).
- [[openscap-auditoria-remota-oscap-ssh-automacao-agentless-bastion]] — Veja também: Varredura Remota Agentless via SSH com **`oscap-ssh`**: Auditando e Remediando Frotas de Servidores Linux sem Instalar Agentes Permanentes.
- [[openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap]] — Referência cruzada direta com openscap-arquitetura-scap-xccdf-oval-cpe-source-data-stream-oscap.
- [[openscap-kubernetes-compliance-operator-cel-scansettingbinding]] — Referência cruzada direta com openscap-kubernetes-compliance-operator-cel-scansettingbinding.

## Fontes
- [OpenSCAP Official GitHub Repository (`OpenSCAP/openscap` — NIST SCAP 1.3 Certified)](https://raw.githubusercontent.com/OpenSCAP/openscap/maint-1.3/README.md) — repositório oficial do motor e utilitário `oscap` certificado pelo NIST cobrindo avaliação XCCDF, OVAL, DataStreams (`ssg-*-ds.xml`), relatórios ARF/HTML e `oscap-ssh`; consultado em 2026-10-03.
- [ComplianceAsCode (`SCAP Security Guide`) Official Repository (`ComplianceAsCode/content`)](https://raw.githubusercontent.com/ComplianceAsCode/content/master/README.md) — repositório oficial de conteúdo SCAP como código contendo perfis CIS, DISA STIG, PCI-DSS, HIPAA e ANSSI e geração de remediações Ansible, Bash, Ignition e Kickstart; consultado em 2026-10-03.
