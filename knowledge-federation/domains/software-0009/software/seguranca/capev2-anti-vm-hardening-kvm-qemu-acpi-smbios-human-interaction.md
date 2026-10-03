---
id: software.seguranca.tranche06.000548
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-06.md"
fontes: ["https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md", "https://capev2.readthedocs.io/en/latest/usage/api.html", "https://github.com/CAPESandbox/CAPE-parsers"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# CAPEv2 Sandbox: Hardening Anti-Detecção de VM (*Anti-VM Cloaking* em KVM/QEMU, SMBIOS/ACPI, Artefatos de Usuário e *Interactive Desktop*)

## Em uma frase
Malwares modernos executam dezenas de verificações ambientais antes de detonar (*Anti-VM* e *Anti-Sandbox*): checam nomes de fabricantes na BIOS/SMBIOS (`QEMU`, `VMware`, `VirtualBox`, `Bochs`), prefixos de endereço MAC (`52:54:00`), tamanho de disco `< 60 GB`, menos de 2 núcleos de CPU, menos de 4 GB de RAM, ausência de histórico de navegação/documentos recentes ou movimento artificial do cursor do mouse.

## Por que importa
Se a VM convidada parecer uma instalação recém-formatada padrão do QEMU com placa de vídeo `QXL` e disco `QEMU HARDDISK`, o malware encerra silenciosamente (`exit(0)`) parecendo benigno.

## Como funciona
A infraestrutura recomendada do CAPEv2 utiliza **KVM/QEMU corrigido** (substituindo todas as strings `QEMU`/`BOCHS` nas tabelas ACPI, SMBIOS, identificadores de disco NVMe/SATA, placas PCI e endereços MAC por identificadores de hardware real Dell/HP/Lenovo), provisiona VMs com >= 4 vCPUs, >= 8 GB RAM e >= 128 GB de disco populado com documentos, histórico de navegador e cookies realistas, além de oferecer o modo **Interactive Desktop** (e **CAPEsolo**) para interação manual com instaladores complexos.

## Exemplo
```xml
<!-- Exemplo de customizacao SMBIOS no XML do libvirt/KVM para ocultar assinatura padrao do hipervisor -->
<os>
  <type arch='x86_64' machine='pc-q35-8.2'>hvm</type>
  <smbios mode='sysinfo'/>
</os>
<sysinfo type='smbios'>
  <bios>
    <entry name='vendor'>Dell Inc.</entry>
    <entry name='version'>1.18.0</entry>
  </bios>
  <system>
    <entry name='manufacturer'>Dell Inc.</entry>
    <entry name='product'>OptiPlex 7090</entry>
  </system>
</sysinfo>
```

## Limites e trade-offs
Jamais instale o pacote completo `spice-vdagent` ou *VMware Tools / VirtualBox Guest Additions* padrão com nomes de processos e drivers facilmente enumeráveis dentro da VM de análise de malware.

## Como verificar
Execute ferramentas públicas de auditoria de detecção de VM (*Pafish* ou *Al-Khaser*) dentro da VM convidada do CAPEv2 e ajuste o XML do KVM até que as checagens de hipervisor passem como máquina física.

## Conexões
- [[capev2-integracao-api-rest-v2-automacao-submissao-thehive-misp]] — Veja também: CAPEv2 Sandbox: Automação via **REST API v2** (`/apiv2/`, Autenticação por Token DRF, `throttling.py` e Integração com Cortex/MISP).
- [[capev2-roteamento-rede-inetsim-tor-vpn-isolamento-pcap]] — Veja também: CAPEv2 Sandbox: Roteamento Por Tarefa (`route=inetsim`, `route=tor`, `route=vpn`, `route=none`) e Prevenção de Abuso Lateral.
- [[capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara]] — Referência cruzada direta com capev2-arquitetura-sandbox-malware-api-hooking-debugger-yara.
- [[capev2-debugger-programavel-assinaturas-yara-breakpoints-anti-sandbox]] — Referência cruzada direta com capev2-debugger-programavel-assinaturas-yara-breakpoints-anti-sandbox.

## Fontes
- [CAPEv2 Official GitHub — Malware Configuration And Payload Extraction](https://raw.githubusercontent.com/kevoreilly/CAPEv2/master/README.md) — documentação oficial do CAPEv2 cobrindo unpacking dinâmico, debugger programável por YARA, AMSI e CAPE-parsers; consultado em 2026-10-03.
- [CAPEv2 Official Documentation — REST API v2 Reference](https://capev2.readthedocs.io/en/latest/usage/api.html) — referência oficial da REST API v2 (/apiv2/), autenticação por token DRF, throttling e endpoints de tarefas; consultado em 2026-10-03.
- [CAPE-parsers Official Repository — Static Configuration Extractors](https://github.com/CAPESandbox/CAPE-parsers) — repositório oficial de extratores de configuração de famílias de malware do CAPEv2; consultado em 2026-10-03.
