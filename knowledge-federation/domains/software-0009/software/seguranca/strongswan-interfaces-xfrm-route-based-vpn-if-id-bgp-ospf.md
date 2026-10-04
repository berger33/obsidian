---
id: software.seguranca.tranche13.001267
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

# VPN Baseada em Rota (**Route-Based VPN**) no strongSwan: Interfaces Virtuais do Kernel Linux (**XFRM Interfaces `xfrmi`** com **`if_id_in` / `if_id_out`**) e BGP/OSPF

## Em uma frase
Qual é a diferença arquitetural entre uma **VPN Baseada em Política (*Policy-Based IPsec*)** tradicional e uma **VPN Baseada em Rota (*Route-Based IPsec*)**, e por que arquitetos de rede e engenheiros de nuvem preferem **Route-Based VPNs com Interfaces XFRM (`xfrmi`)**?

## Por que importa
Na VPN tradicional baseada em política, você precisa declarar estaticamente todas as sub-redes em `local_ts` e `remote_ts`, e o roteamento acontece "por fora" da tabela de rotas normal do Linux (`ip route`), dificultando o uso de protocolos de roteamento dinâmico (**BGP / OSPF com FRRouting ou BIRD**), ECMP (*Equal-Cost Multi-Path*) e regras de firewall por interface!

## Como funciona
A partir do Kernel Linux 4.19+ e do strongSwan moderno, você cria uma **Interface Virtual XFRM (`ip link add ipsec0 type xfrm dev eth0 if_id 42`)** e configura na seção `children` (ou na conexão) do `swanctl.conf`: **`if_id_in = 42`**, **`if_id_out = 42`**, **`local_ts = 0.0.0.0/0, ::/0`** e **`remote_ts = 0.0.0.0/0, ::/0`**! Com isso, toda a decisão de qual tráfego entra no túnel passa a ser controlada simplesmente pela **tabela de rotas padrão do Linux (`ip route add 10.2.0.0/16 dev ipsec0`) ou por uma sessão BGP fechada diretamente sobre a interface `ipsec0`**!

## Exemplo
```bash
# Criar uma interface virtual XFRM (if_id 42) no Kernel Linux e adicionar uma rota padrão de sub-rede apontando para ela
ip link add ipsec0 type xfrm dev eth0 if_id 42
ip addr add 169.254.42.1/30 dev ipsec0
ip link set ipsec0 up
ip route add 10.2.0.0/16 dev ipsec0
```

## Limites e trade-offs
Por que as **XFRM Interfaces (`type xfrm if_id <N>`)** são muito superiores às antigas interfaces `VTI` (`Virtual Tunnel Interface`)? Porque as interfaces XFRM suportam nativamente **IPv4 e IPv6 simultaneamente (Dual-Stack) na mesma interface**, não exigem consumir IPs públicos de túnel na criação do link e permitem associar múltiplos túneis com `if_id` distintos sobre a mesma placa de rede física!

## Como verificar
Além disso, como `ipsec0` é uma interface de rede Linux real, você pode rodar **`tcpdump -ni ipsec0`** para inspecionar o tráfego descriptografado em tempo real e aplicar regras `nftables` (`iifname "ipsec0"`) com clareza total!

## Conexões
- [[strongswan-criptografia-pos-quantica-pqc-ikev2-rfc9370-ml-kem-hibrido]] — Veja também: VPNs **Pós-Quânticas Híbridas (PQC)** no strongSwan: Implementando **RFC 9370 (*Multiple Key Exchanges in IKEv2*)** com **ML-KEM (`ke1_mlkem768` / `mlkem1024`)**.
- [[strongswan-validacao-revogacao-certificados-crl-ocsp-authorities]] — Veja também: Autoridades Certificadoras (**`authorities`**), Validação **OCSP / CRL** e Políticas Estritas de Revogação (`revocation = strict`) no strongSwan.
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[strongswan-estrutura-swanctl-conf-connections-children-secrets-pools]] — Referência cruzada direta com strongswan-estrutura-swanctl-conf-connections-children-secrets-pools.
- [[strongswan-operacao-diagnostico-swanctl-list-sas-ip-xfrm-tcpdump]] — Referência cruzada direta com strongswan-operacao-diagnostico-swanctl-list-sas-ip-xfrm-tcpdump.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
