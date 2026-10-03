---
id: software.seguranca.tranche08.000739
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-08.md"
fontes: ["https://raw.githubusercontent.com/latchset/clevis/master/README.md", "https://raw.githubusercontent.com/latchset/tang/master/README.md", "https://github.com/latchset/jose"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Arquitetura de Segurança de Rede para **Tang (NBDE)**: Segmentação de VLAN de Boot, *802.1X MACsec* e Riscos de Exposição do Endpoint `/rec`

## Em uma frase
Como o protocolo Tang foi desenhado especificamente para provar **presença na rede autorizada** sem exigir que o cliente armazene credenciais de autenticação (que seriam roubadas junto com o disco se o servidor fosse furtado!), **qualquer host que consiga enviar pacotes TCP HTTP `POST /rec/<kid>` para a porta do servidor Tang poderá realizar a operação matemática de recuperação para os seus próprios JWEs**!

## Por que importa
Isso significa que **expor a porta de um servidor Tang diretamente na internet pública, em uma rede Wi-Fi corporativa aberta ou através de um NAT acessível externamente destrói completamente o modelo de segurança do NBDE**: se um ladrão roubar o servidor físico do datacenter, levá-lo para casa e conseguir alcançar o servidor Tang pela internet, o servidor roubado dará boot e decifrará o disco normalmente!

## Como funciona
Portanto, a arquitetura de rede obrigatória para o Tang exige: **(1)** isolar os servidores Tang em uma **VLAN de gerência/storage interna do datacenter** estritamente bloqueada no firewall de borda e inacessível via VPN de usuários comuns; **(2)** habilitar autenticação de porta de switch (**IEEE 802.1X / MACsec**) nos racks físicos; e **(3)** combinar sempre **`tang` + `tpm2`** via Pin **`sss` (`"t": 2`)**.

## Exemplo
```nft
# Regra nftables no servidor Tang permitindo conexoes na porta 80/TCP exclusivamente da sub-rede de servidores do Datacenter
table inet tang_filter {
    chain input {
        type filter hook input priority 0; policy drop;
        ct state established,related accept
        iifname "lo" accept
        ip saddr 10.40.10.0/24 tcp dport 80 accept
    }
}
```

## Limites e trade-offs
Nunca publique o serviço Tang em um Ingress público nem permita roteamento a partir de sub-redes de VPN de trabalho remoto (`Road Warrior VPN`) ou redes de visitantes para o IP do servidor Tang.

## Como verificar
Realize um teste de conectividade a partir de uma sub-rede de usuários/VPN externa confirmando que a conexão TCP para o IP:porta do servidor Tang é bloqueada pelo firewall.

## Conexões
- [[clevis-pin-pkcs11-smartcards-yubikey-desbloqueio-discos-luks]] — Veja também: Clevis Pin **`pkcs11`**: Desbloqueio de Volumes LUKS2 com SmartCards e Tokens de Hardware **PKCS#11** via URI RFC 7512.
- [[clevis-monitoramento-auditoria-logs-tangd-alertas-desbloqueio-anomalo]] — Veja também: Observabilidade e Detecção de Intrusão no **Tang / NBDE**: Monitoramento de Requisições `POST /rec/` e Alertas de Desbloqueio Fora de Janela.
- [[clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow]] — Referência cruzada direta com clevis-arquitetura-nbde-tang-mccallum-relyea-ecmr-sem-escrow.
- [[clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2]] — Referência cruzada direta com clevis-politicas-quorum-shamir-secret-sharing-sss-tang-tpm2.

## Fontes
- [Clevis Official GitHub — Automated Decryption Framework & Pins (tang, tpm2, sss, pkcs11)](https://raw.githubusercontent.com/latchset/clevis/master/README.md) — documentação oficial do framework Clevis cobrindo pins tang, tpm2, sss (Shamir Secret Sharing), pkcs11 e integração LUKS2/initramfs; consultado em 2026-10-03.
- [Tang Official GitHub — Stateless Network-Bound Cryptographic Server & ECMR Protocol](https://raw.githubusercontent.com/latchset/tang/master/README.md) — documentação oficial do servidor Tang cobrindo protocolo McCallum-Relyea (ECMR), geração/rotação de chaves JWK e operação stateless; consultado em 2026-10-03.
- [Latchset JOSE Official C Library & CLI Reference](https://github.com/latchset/jose) — repositório oficial da biblioteca e utilitário jose para objetos JWE/JWK/JWS utilizados pelo Clevis e Tang; consultado em 2026-10-03.
