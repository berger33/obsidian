---
id: software.seguranca.tranche07.000608
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

# `testssl.sh`: Simulação de Handshake de Clientes (`-c` / `--client-simulation`) e Cálculo de **Rating Qualys SSL Labs** (`--rating`)

## Em uma frase
A opção **`-c` (`--client-simulation`)** simula handshakes reais enviando exatamente os pacotes `ClientHello` (versões, lista ordenada de cifras, extensões TLS e curvas) de dezenas de clientes reais (Chrome, Firefox, Safari, Edge, Android, iOS, OpenSSL, Java, Go, Python, cURL, Windows Server/Schannel).

## Por que importa
Antes de endurecer a configuração TLS de um balanceador de carga removendo cifras antigas ou exigindo apenas curvas específicas, a simulação de clientes responde com exatidão se algum cliente legado crítico (ex.: um cliente Java 8 de parceiro B2B ou um terminal Android industrial) perderá conectividade.

## Como funciona
Ao final de uma execução padrão, o `testssl.sh` calcula automaticamente a nota final (**Rating de `A+` a `F` / `T`**) seguindo a especificação pública do *Qualys SSL Labs Server Rating Guide*, penalizando certificados inválidos, protocolos antigos (`TLS 1.0/1.1` limita a nota a `B`) ou ausência de Forward Secrecy.

## Exemplo
```bash
# Simular handshakes de clientes reais (-c) para validar compatibilidade antes de mudanca de politica TLS
testssl.sh -c https://api.internal.corp:443
```

## Limites e trade-offs
Para atingir a nota máxima **`A+`** no rating, o servidor deve suportar TLS 1.3 (e TLS 1.2 apenas com cifras AEAD/PFS), apresentar cadeia X.509 íntegra, não possuir vulnerabilidades e enviar o cabeçalho **HSTS** com `max-age >= 180 dias`.

## Como verificar
Verifique na tabela `Running client simulations` qual protocolo e qual suíte de cifra cada cliente negocia com o servidor.

## Conexões
- [[testssl-cabecalhos-seguranca-http-hsts-hpkp-cookies-banners]] — Veja também: `testssl.sh`: Inspeção de Cabeçalhos de Segurança HTTP (`-h` — HSTS, CSP, X-Frame-Options, Cookies `Secure`/`HttpOnly` e Banners de Servidor).
- [[testssl-varredura-massa-file-nmap-gnmap-parallel-json-html-csv]] — Veja também: `testssl.sh`: Varredura em Massa (`--file` / `-iL`, Entrada Nmap `-oG`), Execução Paralela (`--parallel`) e Relatórios Estruturados (`--jsonfile`, `--csvfile`, `--htmlfile`).
- [[testssl-auditoria-protocolos-tls12-tls13-quic-alpn-npn]] — Referência cruzada direta com testssl-auditoria-protocolos-tls12-tls13-quic-alpn-npn.
- [[testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem]] — Referência cruzada direta com testssl-categorias-cifras-forward-secrecy-curvas-elipticas-mlkem.

## Fontes
- [testssl.sh Official Documentation — testssl.1 Manual Reference](https://testssl.sh/doc/testssl.1.md) — manual oficial do testssl.sh cobrindo auditoria TLS/SSL via sockets TCP, protocolos, cifras, STARTTLS, vulnerabilidades e saída JSON/CSV/HTML; consultado em 2026-10-03.
- [testssl.sh Official GitHub Repository — drwetter/testssl.sh](https://github.com/drwetter/testssl.sh) — repositório oficial do testssl.sh com suporte a curvas elípticas, grupos híbridos pós-quânticos ML-KEM e binários OpenSSL estáticos; consultado em 2026-10-03.
- [testssl.sh Project Organization — testssl/testssl.sh](https://github.com/testssl/testssl.sh) — organização oficial do projeto testssl.sh; consultado em 2026-10-03.
