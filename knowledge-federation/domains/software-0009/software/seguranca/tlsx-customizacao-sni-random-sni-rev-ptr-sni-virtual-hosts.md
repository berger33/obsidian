---
id: software.seguranca.tranche09.000836
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-09.md"
fontes: ["https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md", "https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod", "https://docs.projectdiscovery.io/tools/tlsx/overview"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `tlsx`: Manipulação Avançada de **TLS SNI (`-sni`, `-random-sni`, `-rev-ptr-sni`)** para Descoberta de *Virtual Hosts* e Bypass de Roteamento

## Em uma frase
Na extensão **SNI (*Server Name Indication*, RFC 6066)** do `ClientHello` TLS, o cliente informa em texto claro qual nome de domínio deseja acessar para que o servidor escolha qual certificado X.509 apresentar.

## Por que importa
O comportamento de um servidor web ou proxy reverso quando recebe diferentes valores de SNI revela informações valiosas que o `tlsx` explora com três flags dedicadas: **(1) `-sni <lista_ou_arquivo>`** (conecta em um IP enviando nomes SNI customizados para descobrir certificados de Virtual Hosts internos!), **(2) `-rs` / `-random-sni`** (envia um SNI aleatório para forçar o servidor a revelar seu certificado *default/fallback*!) e **(3) `-rps` / `-rev-ptr-sni`** (faz uma consulta DNS reversa `PTR` do IP antes da conexão e usa automaticamente o hostname retornado pelo `PTR` como SNI do handshake TLS!)!

## Como funciona
A flag **`-rev-ptr-sni` (`-rps`)** é brilhante ao varrer blocos CIDR puros: muitos servidores rejeitam conexões TLS diretas por IP (sem SNI), mas entregam o certificado verdadeiro assim que o `tlsx` injeta o nome descoberto no `PTR` dentro do SNI!

## Exemplo
```bash
# Varrer um bloco de IPs resolvendo o PTR reverso automaticamente para preencher o campo SNI do ClientHello (-rev-ptr-sni)
tlsx -u 10.20.30.0/24 \
  -rev-ptr-sni \
  -san -cn \
  -json -o /cases/easm/ptr_sni_certs.jsonl
```

## Limites e trade-offs
Você também pode usar `-u <IP_DO_SERVIDOR> -sni /cases/pentest/vhost_candidates.txt -san -cn -mm` para descobrir quais nomes de *Virtual Host* possuem um certificado dedicado válido configurado naquele balanceador!

## Como verificar
Compare o certificado retornado conectando no IP com `-random-sni` vs conectando com `-sni dominio.interno.corp`.

## Conexões
- [[tlsx-enumeracao-versoes-tls-version-enum-cipher-enum-cipher-type]] — Veja também: `tlsx`: Enumeração de **Versões TLS Suportadas (`-ve` / `-version-enum`)** e Auditoria de **Cifras Fracas/Inseguras (`-ce` / `-cipher-enum`, `-ct`)**.
- [[tlsx-exportacao-cadeia-pem-certificate-tls-chain-client-server-hello]] — Veja também: `tlsx`: Exportação Completa da **Cadeia de Certificados em PEM (`-cert`, `-tls-chain`)** e Transcrição **`-client-hello` / `-server-hello`**.
- [[tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto]] — Referência cruzada direta com tlsx-arquitetura-coletor-tls-modos-ctls-ztls-openssl-auto.
- [[tlsx-descoberta-subdominios-certificados-san-cn-dns-cidr-asn]] — Referência cruzada direta com tlsx-descoberta-subdominios-certificados-san-cn-dns-cidr-asn.
- [[gobuster-enumeracao-virtual-hosts-vhost-append-domain-filtros]] — Referência cruzada direta com gobuster-enumeracao-virtual-hosts-vhost-append-domain-filtros.

## Fontes
- [ProjectDiscovery tlsx Official GitHub — Fast and Configurable TLS Grabber Focused on TLS Data Collection](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/README.md) — repositório oficial do ProjectDiscovery tlsx cobrindo os 4 motores TLS, extração SAN/CN, auditoria de certificados/cifras e hashes JA3/JARM; consultado em 2026-10-03.
- [ProjectDiscovery tlsx Official Documentation — Scan Modes & Certificate Analysis](https://raw.githubusercontent.com/projectdiscovery/tlsx/main/go.mod) — documentação oficial do tlsx na plataforma ProjectDiscovery Docs; consultado em 2026-10-03.
- [Go Package Documentation — github.com/projectdiscovery/tlsx](https://docs.projectdiscovery.io/tools/tlsx/overview) — referência técnica do pacote Go `projectdiscovery/tlsx`; consultado em 2026-10-03.
