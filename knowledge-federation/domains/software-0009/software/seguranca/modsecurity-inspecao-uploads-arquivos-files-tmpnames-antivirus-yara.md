---
id: software.seguranca.tranche13.001260
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
fontes: ["https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md", "https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Proteção contra **Upload de Webshells e Malware** no ModSecurity: Inspecionando `FILES`, `FILES_TMPNAMES` e Integrando **`@inspectFile`** com **YARA / ClamAV**

## Em uma frase
Funcionalidades de upload de arquivos (`multipart/form-data`, como envio de currículos, fotos de perfil, comprovantes ou anexos de chamados) estão entre os vetores mais visados por atacantes para tentar plantar **Webshells (`.php`, `.jsp`, `.aspx`, `.phar`)** ou arquivos maliciosos no servidor.

## Por que importa
Como o ModSecurity v3 protege o fluxo de upload de arquivos em tempo real antes mesmo que o backend receba o arquivo?

## Como funciona
Em duas camadas: **(1) Validação de Nomes e Extensões (`FILES` e `FILES_NAMES`)** — bloqueando imediatamente extensões executáveis de servidor ou extensões duplas maliciosas (`shell.php.jpg`); e **(2) Inspeção Profunda do Conteúdo Temporário (`FILES_TMPNAMES` com `@inspectFile`)** — quando `SecUploadKeepFiles RelevantOnly` (ou `On`) e `SecTmpDir /tmp/modsec` estão configurados, o ModSecurity extrai o arquivo do stream `multipart/form-data` para um diretório temporário isolado e executa um script verificador via **`@inspectFile`** (que pode rodar **YARA** ou **ClamAV `clamdscan`** sobre os bytes reais do arquivo!). Se o verificador detectar uma webshell ou malware (mesmo disfarçada dentro dos metadados EXIF de uma imagem `.jpg`!), o ModSecurity **aborta a requisição com `403 Forbidden` e apaga o arquivo temporário antes que a aplicação web sequer saiba que o upload existiu**!

## Exemplo
```apache
# Inspecionar todo arquivo enviado via upload multipart executando um verificador YARA/ClamAV antes de entregar a requisicao ao backend
SecTmpDir /var/cache/modsecurity/tmp
SecUploadDir /var/cache/modsecurity/upload
SecUploadKeepFiles RelevantOnly
SecUploadFileMode 0600

SecRule FILES_TMPNAMES "@inspectFile /etc/nginx/modsec/scan_upload_yara.sh" \
    "id:100600,phase:2,deny,status:403,log,t:none,msg:'Upload bloqueado: Webshell ou Malware detectado pelo scanner YARA/ClamAV'"
```

## Limites e trade-offs
O script chamado por **`@inspectFile`** recebe o caminho do arquivo temporário como primeiro argumento (`$1`) e segue a convenção do ModSecurity: se imprimir uma linha começando com **`0`** (ex.: `0 Webshell detectada`), o operador considera que a regra deu *match* (bloqueando o upload!); se imprimir **`1`** (ex.: `1 OK`), o arquivo é considerado limpo e liberado!

## Como verificar
Defina sempre **`SecUploadFileMode 0600`** e monte o diretório `/var/cache/modsecurity/tmp` com as flags de montagem do Linux **`noexec,nosuid,nodev`**!

## Conexões
- [[modsecurity-virtual-patching-cve-zero-day-mitigacao-imediata-borda]] — Veja também: Aplicando **Virtual Patching** no ModSecurity v3: Mitigando **Zero-Days e CVEs Críticas** na Borda em Minutos Enquanto o Código da Aplicação é Corrigido.
- [[modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy]] — Referência cruzada direta com modsecurity-arquitetura-libmodsecurity-v3-conectores-nginx-apache-envoy.
- [[modsecurity-processadores-body-json-xml-limites-anti-dos-pcre]] — Referência cruzada direta com modsecurity-processadores-body-json-xml-limites-anti-dos-pcre.

## Fontes
- [OWASP ModSecurity v3 (`libmodsecurity`) Official GitHub](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/README.md) — repositório oficial do OWASP ModSecurity v3 detalhando a arquitetura standalone da biblioteca `libmodsecurity`, conectores Nginx/Apache, PCRE2, `libinjection` e YAJL JSON; consultado em 2026-10-03.
- [OWASP ModSecurity v3 Recommended Configuration (`modsecurity.conf-recommended`)](https://raw.githubusercontent.com/owasp-modsecurity/ModSecurity/v3/master/modsecurity.conf-recommended) — configuração oficial recomendada do ModSecurity v3 cobrindo `SecRuleEngine`, `SecRequestBodyAccess`, processadores XML/JSON, limites anti-DoS e `SecAuditLogFormat JSON`; consultado em 2026-10-03.
