---
id: software.seguranca.tranche08.000777
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
fontes: ["https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md", "https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown", "https://github.com/robertdavidgraham/masscan"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Masscan: Customização de Requisições HTTP (`--http-user-agent`, `--http-header`, `--http-method`), Captura de **Certificados TLS X.509** e Checagens **SMB / VULN**

## Em uma frase
Quando o Masscan é executado com **`--banners`** em portas HTTP (`80`, `8080`, `8000`) e HTTPS/SSL (`443`, `8443`), sua pilha TCP/TLS em user-space envia uma requisição HTTP padrão (ou um `ClientHello` TLS) e faz o parsing estruturado dos cabeçalhos de resposta, do `<title>` HTML e dos campos do certificado **X.509 (Subject, Issuer, SANs, Serial, Validade)**!

## Por que importa
Conforme detalhado no manual `doc/masscan.8.markdown`, você pode customizar completamente o probe HTTP enviado pelo Masscan usando **`--http-user-agent "<string>"`**, **`--http-header "Name: Value"`**, **`--http-method GET`**, **`--http-url "/healthz"`** e **`--http-field-remove`** — permitindo varrer uma sub-rede inteira procurando um endpoint específico de healthcheck ou painel administrativo em uma única passagem!

## Como funciona
Além disso, o parser de protocolos embutido do Masscan extrai informações nativas de **SMB v1/v2 (domínio Active Directory, nome NetBIOS, versão do Windows e assinatura SMB)** na porta `445` e possui módulos de verificação como `--heartbleed` e `--vuln`.

## Exemplo
```bash
# Capturar banners HTTP/TLS e metadados SMB em uma sub-rede customizando o User-Agent e a rota HTTP requisitada
sudo iptables -I INPUT -p tcp --dport 61001 -j DROP
sudo masscan 10.20.0.0/16 -p80,443,445,8080,8443 \
  --banners \
  --adapter-port 61001 \
  --http-user-agent "SecOps-Internal-Inventory/2026" \
  --http-url "/" \
  --rate 1500 \
  -oJ /cases/easm/http_tls_smb_inventory.json
sudo iptables -D INPUT -p tcp --dport 61001 -j DROP
```

## Limites e trade-offs
Como o Masscan conecta por endereço IP, ao varrer HTTPS (`443`) com `--banners` ele captura o certificado TLS padrão retornado pelo IP, revelando nos campos *Subject CN* e *Subject Alternative Name (SAN)* os nomes de domínio reais configurados naquele servidor!

## Como verificar
Extraia todos os certificados X.509 e banners SMB do JSON resultante com `jq '.[] | select(.ports[].service.name == "ssl" or .ports[].service.name == "smb")' /cases/easm/http_tls_smb_inventory.json`.

## Conexões
- [[masscan-payloads-udp-nmap-payloads-pcap-payloads-customizados]] — Veja também: Masscan: Varredura de Portas **UDP (`-pU:53,123,161,500`)**, Uso de **`--nmap-payloads`** e Injeção de Payloads UDP Customizados (`--pcap-payloads`).
- [[masscan-integracao-dois-estagios-masscan-descoberta-nmap-profundo]] — Veja também: Arquitetura de Varredura em **Dois Estágios**: Descoberta Rápida de Portas (`0-65535`) com **Masscan** + Fingerprinting Profundo (`-sV -sC`) com **Nmap**.
- [[masscan-captura-banners-pilha-tcp-conflito-kernel-rst-source-ip-iptables]] — Referência cruzada direta com masscan-captura-banners-pilha-tcp-conflito-kernel-rst-source-ip-iptables.

## Fontes
- [Masscan Official GitHub — Mass IP Port Scanner Architecture & Banner Checking](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/README.md) — documentação oficial do Masscan cobrindo transmissão assíncrona, cifra BlackRock, captura de banners, prevenção de TCP RST e PF_RING; consultado em 2026-10-03.
- [Masscan Official Manual Page — masscan(8) Complete CLI & Configuration Reference](https://raw.githubusercontent.com/robertdavidgraham/masscan/master/doc/masscan.8.markdown) — manual oficial masscan(8) cobrindo taxas, excludefile, paused.conf, shards, formatos binários/JSON/XML e payloads UDP/HTTP; consultado em 2026-10-03.
- [Masscan Project Repository — robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) — repositório oficial do código-fonte do Masscan; consultado em 2026-10-03.
