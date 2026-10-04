---
id: software.seguranca.tranche08.000743
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
fontes: ["https://docs.mitmproxy.org/stable/concepts/modes/", "https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md", "https://docs.mitmproxy.org/stable/addons-overview/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# mitmproxy: Gestão da CA Dinâmica (`~/.mitmproxy/`, Domínio Mágico **`mitm.it`**), Certificados de Cliente **mTLS** (`--certs` / `--client-certs`) e `SSLKEYLOGFILE`

## Em uma frase
Na primeira execução, o `mitmproxy` gera localmente em **`~/.mitmproxy/`** uma Autoridade Certificadora (CA) exclusiva daquela instalação (`mitmproxy-ca.pem` com a chave privada + certificado, e `mitmproxy-ca-cert.pem` / `.p12` / `.cer` contendo apenas o certificado público da CA para instalação nos dispositivos de teste).

## Por que importa
Para decifrar uma conexão HTTPS em tempo real (*On-the-Fly Certificate Generation*), o `mitmproxy` lê o **SNI** do `ClientHello` (e o certificado real do servidor upstream), gera instantaneamente em memória um certificado folha para aquele domínio assinado pela sua CA local e completa o handshake TLS.

## Como funciona
Quando o aplicativo auditado exige **autenticação mútua TLS (mTLS)** perante o servidor backend, basta passar **`--set client_certs=/caminho/cert_cliente.pem`** para que o `mitmproxy` apresente o certificado de cliente ao servidor upstream; e exportar **`SSLKEYLOGFILE=/cases/pcaps/mitm_tls_keys.log`** faz o `mitmproxy` gravar todos os segredos de sessão TLS para inspeção paralela no Wireshark!

## Exemplo
```bash
# Executar o mitmdump apresentando certificado de cliente mTLS ao servidor upstream e exportando chaves TLS para o Wireshark
SSLKEYLOGFILE=/cases/pcaps/mitm_tls_keys.log \
mitmdump --set client_certs=/cases/pentest/mtls_client_bundle.pem \
  --set ssl_version_client_min=TLS1_2 \
  -w /cases/pentest/mtls_session.mitm
```

## Limites e trade-offs
Trate o arquivo **`~/.mitmproxy/mitmproxy-ca.pem`** (que contém a chave privada da CA que você instalou no dispositivo de teste) com o mesmo rigor de uma chave privada root: **jamais compartilhe o `mitmproxy-ca.pem` nem deixe a CA de teste instalada em smartphones de uso pessoal após o encerramento do pentest**!

## Como verificar
Verifique que `~/.mitmproxy/mitmproxy-ca.pem` possui permissão `0600` e use apenas `mitmproxy-ca-cert.pem` (sem a chave privada) ao importar no dispositivo de teste.

## Conexões
- [[mitmproxy-modos-operacao-regular-local-ebpf-wireguard-transparent-reverse]] — Veja também: mitmproxy: Os 9 Modos de Operação (`regular`, **`local` via eBPF/OS**, **`wireguard`** User-Space, `reverse`, `transparent`, `tun`, `upstream`, `socks5` e `dns`).
- [[mitmproxy-expressoes-filtro-flow-filters-interceptacao-seletiva]] — Veja também: mitmproxy: Linguagem de **Expressões de Filtro de Fluxo (*Flow Filter Expressions*)** para Visualização (`v`), Interceptação (`i`) e Exportação.
- [[mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb]] — Referência cruzada direta com mitmproxy-arquitetura-tres-interfaces-mitmproxy-mitmdump-mitmweb.
- [[wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab]] — Referência cruzada direta com wireshark-decriptacao-tls13-sslkeylogfile-dsb-kerberos-keytab.
- [[testssl-evasao-ids-sneaky-sni-vhost-mtls-client-certs-cicd]] — Referência cruzada direta com testssl-evasao-ids-sneaky-sni-vhost-mtls-client-certs-cicd.

## Fontes
- [mitmproxy Official Documentation — Proxy Modes (Regular, Local eBPF, WireGuard, Reverse, Transparent, SOCKS5, DNS)](https://docs.mitmproxy.org/stable/concepts/modes/) — documentação oficial dos nove modos de operação do mitmproxy incluindo captura local por processo e servidor WireGuard em user-space; consultado em 2026-10-03.
- [mitmproxy Official GitHub — Interactive TLS-Capable Intercepting Proxy](https://raw.githubusercontent.com/mitmproxy/mitmproxy/main/README.md) — repositório oficial do projeto mitmproxy cobrindo mitmproxy, mitmdump e mitmweb; consultado em 2026-10-03.
- [mitmproxy Official Documentation — Python Addons & Event Hooks Architecture](https://docs.mitmproxy.org/stable/addons-overview/) — guia oficial de desenvolvimento de addons em Python e hooks de ciclo de vida de fluxos HTTP, WebSocket, TCP, UDP e DNS; consultado em 2026-10-03.
