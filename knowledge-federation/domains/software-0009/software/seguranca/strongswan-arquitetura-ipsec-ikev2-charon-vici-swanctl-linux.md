---
id: software.seguranca.tranche13.001261
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/strongswan/strongswan/master/README.md", "https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura Moderna do **strongSwan (`strongswan/strongswan`)**: Daemon **`charon`**, Protocolo **`vici`** e Configuração Declarativa **`swanctl.conf`**

## Em uma frase
Quando uma empresa precisa fechar um túnel **IPsec / IKEv2** padronizado pela IETF com gateways de nuvem (**AWS Site-to-Site VPN**, **Google Cloud VPN**, **Azure VPN Gateway**), firewalls corporativos (FortiGate, Palo Alto, Cisco) ou clientes nativos de Windows, macOS, iOS e Android (que já vêm com cliente IKEv2 embutido de fábrica no sistema operacional!), qual é a solução open-source padrão mundial no Linux?

## Por que importa
O **strongSwan** consolida o plano de controle IKEv2 em espaço de usuário com o plano de dados XFRM de altíssima vazão no Kernel Linux.

## Como funciona
Nas versões modernas (5.x/6.x), o strongSwan abandonou o antigo formato legado `ipsec.conf` / `ipsec.secrets` (`starter` / `stroke`) em favor de uma arquitetura moderna, modular e totalmente programável composta por três elementos: **(1) O daemon IKE `charon` (`charon-systemd`)**, que negocia as associações de segurança **IKEv2 (`RFC 7296`, UDP 500 / 4500 NAT-T)** em espaço de usuário e instala as chaves de criptografia de pacotes **ESP (`Encapsulating Security Payload`)** diretamente no subsistema **XFRM do Kernel Linux** via Netlink; **(2) O protocolo IPC `vici` (*Versatile IKE Configuration Interface*)**; e **(3) A ferramenta de controle `swanctl`**, que lê o arquivo declarativo **`/etc/swanctl/swanctl.conf`**!

## Exemplo
```bash
# Carregar todas as configuracoes, certificados e credenciais de /etc/swanctl/swanctl.conf no daemon charon via protocolo vici
swanctl --load-all
swanctl --stats
```

## Limites e trade-offs
Por que o Kernel Linux processa o tráfego de dados do **IPsec (`ESP` via XFRM)** em velocidades de dezenas de Gigabits por segundo? Porque o daemon `charon` em espaço de usuário atua **apenas no plano de controle** (autenticando os pares, negociando IKEv2 e fazendo o *rekeying* periódico das chaves); uma vez que as chaves `AES-GCM-256` ou `ChaCha20-Poly1305` são instaladas na tabela XFRM do kernel, **100% dos pacotes IP são cifrados e decifrados diretamente dentro do Kernel Linux com aceleração de hardware (`AES-NI`) ou offloading de placa de rede (`XFRM Hardware Offload`)**!

## Como verificar
Nunca misture o legado `ipsec.conf` com o moderno `swanctl.conf` no mesmo servidor: instale e utilize exclusivamente os pacotes `strongswan-swanctl` e `charon-systemd`.

## Conexões
- [[strongswan-estrutura-swanctl-conf-connections-children-secrets-pools]] — Veja também: Anatomia do **`/etc/swanctl/swanctl.conf`**: As 4 Seções Principais (**`connections`, `children`, `secrets`, `pools`**) e Diretórios `/etc/swanctl/x509*`.
- [[strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap]] — Referência cruzada direta com strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap.
- [[wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia]] — Referência cruzada direta com wireguard-arquitetura-protocolo-vpn-kernel-noise-ikpsk2-criptografia.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
