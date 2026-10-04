---
id: software.seguranca.tranche07.000610
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-07.md"
fontes: ["https://testssl.sh/doc/testssl.1.md", "https://github.com/drwetter/testssl.sh", "https://github.com/testssl/testssl.sh"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# `testssl.sh`: Teste de VirtualHosts (`--ip` / `--SNI`), Autenticação Mútua **mTLS** (`--mtls`), Modo Discreto (`--sneaky`) e Gate de CI/CD

## Em uma frase
Em ambientes com múltiplos VirtualHosts atrás do mesmo IP, proxies reversos ou endpoints protegidos por **mTLS (*Mutual TLS*)**, o `testssl.sh` oferece controle cirúrgico sobre a resolução de endereço, a extensão `Server Name Indication (SNI)` e o certificado de cliente.

## Por que importa
Ao testar um servidor novo em staging antes da virada do DNS público, passar **`--ip <IP_DO_SERVIDOR> https://producao.exemplo.com.br`** força o `testssl.sh` a conectar no IP de staging enviando `producao.exemplo.com.br` na extensão TLS **SNI** e no cabeçalho HTTP `Host`.

## Como funciona
E quando o endpoint exige autenticação mútua por certificado de cliente (**mTLS**), a flag **`--mtls <arquivo_pem>`** (contendo a chave privada e o certificado X.509 do cliente concatenados sem senha) autentica todas as sondas do `testssl.sh` contra o gateway mTLS.

## Exemplo
```bash
# Auditar um endpoint de staging antes da mudanca de DNS (--ip) que exige certificado de cliente (--mtls)
testssl.sh --ip 10.20.30.50 \
  --mtls /etc/secops/certs/auditor_mtls_bundle.pem \
  -p -s -S -U \
  https://payments-api.internal.corp:8443
```

## Limites e trade-offs
Testar todas as 370 cifras e vulnerabilidades históricas (como Heartbleed e CCS Injection) dispara alertas legítimos de IDS/IPS (Suricata/WAF); adicione **`--sneaky`** (usa `User-Agent` comum e reduz pegada) e avise previamente o SOC sobre o IP de origem do scanner.

## Como verificar
Valide em pipeline de homologação que a nota retornada no JSON (`.scanResult[0].rating[].finding`) é `A` ou `A+` antes de promover a configuração do ingress/load balancer para produção.

## Conexões
- [[testssl-varredura-massa-file-nmap-gnmap-parallel-json-html-csv]] — Veja também: `testssl.sh`: Varredura em Massa (`--file` / `-iL`, Entrada Nmap `-oG`), Execução Paralela (`--parallel`) e Relatórios Estruturados (`--jsonfile`, `--csvfile`, `--htmlfile`).
- [[testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa]] — Referência cruzada direta com testssl-inspecao-certificados-x509-cadeia-ocsp-stapling-ct-caa.
- [[certbot-chaves-ecdsa-p256-p384-rsa-ocsp-must-staple-reuse-key]] — Referência cruzada direta com certbot-chaves-ecdsa-p256-p384-rsa-ocsp-must-staple-reuse-key.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
