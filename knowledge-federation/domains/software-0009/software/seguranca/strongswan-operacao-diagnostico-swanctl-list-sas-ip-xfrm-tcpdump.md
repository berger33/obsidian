---
id: software.seguranca.tranche13.001270
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

# Diagnóstico e Troubleshooting Avançado de Túneis IPsec no Linux: **`swanctl --list-sas`**, **`swanctl --log`**, **`ip -s xfrm state/policy`** e NAT-Traversal (`UDP 4500`)

## Em uma frase
Quando um túnel VPN IPsec/IKEv2 não sobe na Fase 1 (`IKE SA`), falha nos seletores de tráfego da Fase 2 (`CHILD SA` com erro `TS_UNACCEPTABLE`) ou sobe mas não passa pacotes entre as duas redes, quais são os 4 comandos essenciais de diagnóstico que todo engenheiro de redes e segurança Linux deve dominar?

## Por que importa
Primeiro, acompanhe a negociação IKEv2 em tempo real no terminal rodando **`swanctl --log`** em uma aba enquanto dispara a conexão manualmente em outra aba com **`swanctl --initiate --child <nome_child>`**! Segundo, inspecione o estado das SAs negociadas, algoritmos eleitos, SPIs e contadores de bytes/pacotes com **`swanctl --list-sas`**!

## Como funciona
Terceiro — e aqui está o segredo para diagnosticar problemas no plano de dados! — consulte diretamente as tabelas **XFRM do Kernel Linux** com **`ip -s xfrm state`** (que mostra as chaves ESP instaladas, contadores de pacotes cifrados/decifrados e se há drops de replay `replay-window` ou integridade!) e **`ip -s xfrm policy`** (que mostra os seletores de tráfego `dir out`, `dir in` e `dir fwd`)!

## Exemplo
```bash
# Inspecionar tuneis ativos, contadores de bytes/pacotes IKEv2 e auditar diretamente as tabelas XFRM de estado e politica no Kernel Linux
swanctl --list-sas
ip -s xfrm state
ip -s xfrm policy
```

## Limites e trade-offs
Como entender rapidamente a transição automática para **NAT-Traversal (`UDP 4500`)** na saída do `swanctl --list-sas`? O IKEv2 inicia a negociação na porta **UDP `500`**, mas durante o primeiro par de mensagens (`IKE_SA_INIT`) ambos os lados trocam hashes dos seus IPs/portas (`NAT_DETECTION_SOURCE_IP` / `DESTINATION_IP`); se houver qualquer NAT no caminho (como ocorre em toda VM na AWS/GCP/Azure que possui um IP privado na placa e um Elastic IP anexado externamente!), o strongSwan **flutua automaticamente na mensagem `IKE_AUTH` para a porta UDP `4500` e encapsula todos os pacotes ESP dentro de UDP `4500` (`encap: espinudp`)**!

## Como verificar
Se `swanctl --list-sas` mostrar que os contadores de bytes `out` aumentam mas `in` permanece em `0`, verifique se o firewall do outro lado está bloqueando `UDP 4500` ou protocolo `ESP (50)`.

## Conexões
- [[strongswan-integracao-hardware-tpm2-pkcs11-hsm-protecao-chaves]] — Veja também: Proteção de Chaves Privadas de VPN em Hardware com o strongSwan: Integração Nativa com **TPM 2.0 (`handle`)**, **Smartcards / YubiKey (`PKCS#11`)** e HSMs.
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[strongswan-interfaces-xfrm-route-based-vpn-if-id-bgp-ospf]] — Referência cruzada direta com strongswan-interfaces-xfrm-route-based-vpn-if-id-bgp-ospf.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
