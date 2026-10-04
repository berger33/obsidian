---
id: software.seguranca.tranche13.001268
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

# Autoridades Certificadoras (**`authorities`**), Validação **OCSP / CRL** e Políticas Estritas de Revogação (`revocation = strict`) no strongSwan

## Em uma frase
O que acontece se o notebook de um funcionário ou o certificado de um gateway de filial for comprometido, você revogar esse certificado na sua Autoridade Certificadora (PKI), mas o seu gateway strongSwan continuar aceitando conexões daquele certificado revogado porque o servidor de revogação OCSP/CRL não foi consultado ou a política padrão era branda?

## Por que importa
Para que a revogação de certificados funcione de forma imediata e determinística em uma VPN IPsec, você deve configurar duas coisas no `swanctl.conf`: **(1) A seção de topo `authorities { ... }`**, onde você vincula o certificado da sua CA (`cacert = ca-interna.pem`) às URLs de distribuição de **Lista de Certificados Revogados (`crl_uris = http://pki.interna/ca.crl`)** e/ou ao respondedor **OCSP (`ocsp_uris = http://ocsp.interna:8080`)**; e **(2) A diretiva `revocation = strict`** dentro do bloco `remote { ... }` da conexão!

## Como funciona
Por que entender a diferença entre `revocation = relaxed` (o padrão), `ifuri` e **`strict`** é vital? No modo `relaxed`, se o servidor OCSP/CRL estiver temporariamente inacessível na rede, o strongSwan apenas registra um aviso e **permite** o túnel; já no modo **`revocation = strict`**, se o status de não-revogação não puder ser confirmado positivamente via OCSP ou CRL fresca, o strongSwan **bloqueia a conexão (*Fail-Closed*)**!

## Exemplo
```text
# Configurar no /etc/swanctl/swanctl.conf uma Autoridade Certificadora (authorities) com verificacao OCSP e CRL
authorities {
    pki-corporativa {
        cacert = ca-raiz-corporativa.pem
        ocsp_uris = http://ocsp.pki.exemplo.br
        crl_uris  = http://crl.pki.exemplo.br/corporativa.crl
    }
}
```

## Limites e trade-offs
Para evitar que uma oscilação momentânea do servidor HTTP de CRL derrube túneis legítimos quando `revocation = strict` estiver ativo, habilite o cache local de CRLs no plugin `revocation` e configure um job `cron`/systemd timer que baixa periodicamente a CRL atualizada para **`/etc/swanctl/x509crl/`** e roda **`swanctl --load-creds`**!

## Como verificar
Use **`swanctl --list-certs --type x509_crl`** para auditar no terminal todas as CRLs atualmente em memória no daemon `charon` e suas datas de validade (`until`).

## Conexões
- [[strongswan-interfaces-xfrm-route-based-vpn-if-id-bgp-ospf]] — Veja também: VPN Baseada em Rota (**Route-Based VPN**) no strongSwan: Interfaces Virtuais do Kernel Linux (**XFRM Interfaces `xfrmi`** com **`if_id_in` / `if_id_out`**) e BGP/OSPF.
- [[strongswan-integracao-hardware-tpm2-pkcs11-hsm-protecao-chaves]] — Veja também: Proteção de Chaves Privadas de VPN em Hardware com o strongSwan: Integração Nativa com **TPM 2.0 (`handle`)**, **Smartcards / YubiKey (`PKCS#11`)** e HSMs.
- [[strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux]] — Referência cruzada direta com strongswan-arquitetura-ipsec-ikev2-charon-vici-swanctl-linux.
- [[strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap]] — Referência cruzada direta com strongswan-vpn-site-to-site-ikev2-pki-certificados-x509-trap.
- [[openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao]] — Referência cruzada direta com openssl-operacoes-pki-ca-x509-req-crl-ocsp-automacao.

## Fontes
- [strongSwan Official GitHub — OpenSource IPsec-Based VPN Solution](https://raw.githubusercontent.com/strongswan/strongswan/master/README.md) — repositório oficial do strongSwan cobrindo arquitetura do daemon `charon`, protocolo `vici`, ferramenta `swanctl`, utilitário `pki` e cenários Site-to-Site/Roadwarrior; consultado em 2026-10-03.
- [strongSwan Official `swanctl.conf` Documentation (`docs.strongswan.org`)](https://docs.strongswan.org/docs/latest/swanctl/swanctlConf.html) — especificação completa do `/etc/swanctl/swanctl.conf` detalhando `connections`, `children`, `secrets`, `pools`, `authorities`, interfaces XFRM (`if_id_in`/`if_id_out`), TPM 2.0 e propostas pós-quânticas `ke1_mlkem768`; consultado em 2026-10-03.
